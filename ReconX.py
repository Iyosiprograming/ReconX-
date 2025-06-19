import requests
from bs4 import BeautifulSoup
import argparse
import hashlib
import re
from colorama import init, Fore, Style

init()

def banner():
    print(Fore.GREEN + r"""
   ______                 __  __  __  __            
  / ____/___  ____  ___  / /_/ /_/ /_/ /_____  _____
 / /   / __ \/ __ \/ _ \/ __/ __/ __/ __/ __ \/ ___/
/ /___/ /_/ / /_/ /  __/ /_/ /_/ /_/ /_/ /_/ / /    
\____/\____/ .___/\___/\__/\__/\__/\__/\____/_/     
          /_/  Web Recon & CMS Fingerprinter      
""" + Fore.CYAN + "\n         Developer: Iyosiyas Ivasyos\n" + Style.RESET_ALL)

def fetch_headers_and_html(url):
    try:
        response = requests.get(url, timeout=10)
        return response.headers, response.text, response
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Request failed: {e}" + Style.RESET_ALL)
        return {}, "", None

def analyze_headers(headers, response):
    print(Fore.YELLOW + "\n[+] Analyzing Headers..." + Style.RESET_ALL)
    server = headers.get("Server", "Unknown")
    powered = headers.get("X-Powered-By", "Unknown")
    content = headers.get("Content-Type", "Unknown")
    cookies = response.cookies

    print(f"    Server: {server}")
    print(f"    X-Powered-By: {powered}")
    print(f"    Content-Type: {content}")

    print(Fore.YELLOW + "\n[+] Host Stack Fingerprint:" + Style.RESET_ALL)
    if "Win" in server:
        print("    OS: Windows (based on Server header)")
    elif "Ubuntu" in server or "Debian" in server:
        print("    OS: Linux - Debian-based")
    elif "CentOS" in server or "Red Hat" in server:
        print("    OS: Linux - RHEL-based")
    elif "FreeBSD" in server:
        print("    OS: FreeBSD")
    else:
        print("    OS: Unknown")

    if "PHP" in powered:
        print(f"    Backend Language: PHP ({powered})")
    elif "ASP.NET" in powered:
        print("    Backend Language: ASP.NET (Windows)")
    elif "Python" in powered:
        print("    Backend Language: Python")
    else:
        print("    Backend Language: Unknown")

    for c in cookies:
        if "PHPSESSID" in c.name:
            print("    Session Type: PHP")
        elif "ASP.NET" in c.name:
            print("    Session Type: ASP.NET")
        elif "laravel_session" in c.name:
            print("    Framework: Laravel")
        elif "JSESSIONID" in c.name:
            print("    Session Type: Java")
    print()

def detect_meta(html):
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"name": "generator"})
    if meta:
        return meta.get("content")
    return None

def detect_js_frameworks(html):
    print(Fore.YELLOW + "[+] Frontend JS Libraries..." + Style.RESET_ALL)
    libs = []
    if "jquery" in html.lower():
        match = re.search(r"jquery[-.]([0-9.]+)", html)
        version = match.group(1) if match else "unknown"
        libs.append(f"jQuery {version}")
    if "react" in html.lower():
        libs.append("React")
    if "angular" in html.lower():
        libs.append("Angular")
    if "vue" in html.lower():
        libs.append("Vue.js")
    if libs:
        for lib in libs:
            print(f"    [+] {lib}")
    else:
        print("    [-] No common JS frameworks found")

def detect_db_errors(html):
    print(Fore.YELLOW + "[+] Database Technology Guess..." + Style.RESET_ALL)
    dbs = {
        "MySQL": ["MySQL server has gone away", "mysql_fetch_array"],
        "PostgreSQL": ["pg_query", "PostgreSQL"],
        "MongoDB": ["MongoDB\\Driver", "MongoError"],
        "MSSQL": ["System.Data.SqlClient", "SqlException"],
    }
    found = False
    for db, signs in dbs.items():
        for sign in signs:
            if sign.lower() in html.lower():
                print(f"    [+] Possible DB: {db} (found '{sign}')")
                found = True
                break
    if not found:
        print("    [-] No DB fingerprint found")

def detect_known_paths(url):
    print(Fore.YELLOW + "[+] CMS Detection..." + Style.RESET_ALL)
    paths = {
        "WordPress": "/wp-login.php",
        "Joomla": "/administrator/",
        "Drupal": "/user/login",
        "Moodle": "/login/index.php",
    }
    for cms, path in paths.items():
        try:
            r = requests.get(url.rstrip("/") + path, timeout=5)
            if r.status_code == 200:
                print(Fore.GREEN + f"    [+] {cms} detected via {path}" + Style.RESET_ALL)
        except:
            continue

def detect_login_form(html):
    soup = BeautifulSoup(html, "html.parser")
    forms = soup.find_all("form")
    for form in forms:
        if "login" in str(form).lower() and "username" in str(form).lower():
            print(Fore.GREEN + "    [+] Login form structure matches common CMS login" + Style.RESET_ALL)
            break

def detect_meta_cms(url, html):
    found = False
    meta = detect_meta(html)
    if meta:
        print(Fore.GREEN + f"    [+] Meta Tag Detected: {meta}" + Style.RESET_ALL)
        found = True
    detect_known_paths(url)
    detect_login_form(html)
    return found

def main():
    parser = argparse.ArgumentParser(description="Advanced Web Recon Tool")
    parser.add_argument("url", help="Target URL (e.g. http://site.com)")
    args = parser.parse_args()

    banner()
    print(Fore.CYAN + f"[+] Scanning Target: {args.url}" + Style.RESET_ALL)

    headers, html, response = fetch_headers_and_html(args.url)
    if headers and html:
        analyze_headers(headers, response)
        detect_meta_cms(args.url, html)
        detect_js_frameworks(html)
        detect_db_errors(html)

if __name__ == "__main__":
    main()