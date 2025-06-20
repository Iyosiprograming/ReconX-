
# 🕵️‍♂️ ReconX - Advanced Web Reconnaissance & CMS Fingerprinting Tool

**ReconX** is a smart, passive reconnaissance tool built for ethical hackers and penetration testers. It detects web technologies used by a target — including server stack, CMS, backend frameworks, frontend JS libraries, and even possible database technologies — **all from a single request**.

> 🔧 Built by [Iyosiyas Ivasyos](#) — Cybersecurity Researcher & Ethical Hacker studnet

---

## 🚀 Features

- 🧠 **Intelligent Stack Fingerprinting**
  - Detects server software (Apache, Nginx, IIS)
  - Guesses OS (Windows, Linux, FreeBSD) via headers
  - Identifies backend language (PHP, Python, ASP.NET)
  - Recognizes frameworks (Laravel, Django, Flask)
- 📚 **CMS Detection**
  - Finds CMS via meta tags (`<meta name="generator">`)
  - Detects known paths like `/wp-login.php`, `/administrator/`
  - Analyzes login form structure
- 🎯 **Frontend Detection**
  - Scans for common JS libraries like jQuery, React, Angular, Vue.js
  - Parses versions from script tags
- 🗄️ **Database Leak Guessing**
  - Flags common error messages from MySQL, PostgreSQL, MongoDB, MSSQL
- 🎨 **Color-coded Output**
  - CLI styled for clarity, with banners and section highlights

---

## 📸 Demo

```bash
$ python reconX.py http://testphp.vulnweb.com
````

```
   ______                 __  __  __  __            
  / ____/___  ____  ___  / /_/ /_/ /_/ /_____  _____
 / /   / __ \/ __ \/ _ \/ __/ __/ __/ __/ __ \/ ___/
/ /___/ /_/ / /_/ /  __/ /_/ /_/ /_/ /_/ /_/ / /    
\____/\____/ .___/\___/\__/\__/\__/\__/\____/_/     
          /_/  Web Recon & CMS Fingerprinter      

         Developer: Iyosiyas Ivasyos

[+] Scanning Target: http://testphp.vulnweb.com

[+] Analyzing Headers...
    Server: Apache/2.4.54 (Debian)
    X-Powered-By: PHP/8.1.12
    Content-Type: text/html

[+] Host Stack Fingerprint:
    OS: Linux - Debian-based
    Backend Language: PHP (8.1.12)
    Session Type: PHP
    Framework: Laravel

[+] CMS Detection...
    [+] WordPress detected via /wp-login.php
    [+] Meta Tag Detected: WordPress 6.2
    [+] Login form structure matches common CMS login

[+] Frontend JS Libraries...
    [+] jQuery 3.6.0
    [+] React

[+] Database Technology Guess...
    [+] Possible DB: MySQL (found 'mysql_fetch_array')
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/Iyosiprograming/ReconX-.git
cd reconx
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ✅ Python 3.13.2 required

---

## 🧪 Usage

```bash
python reconX.py http://targetsite.com
```

It will automatically scan headers, HTML content, and guess technologies used by the target system.

---

## 📦 Requirements

* `requests`
* `beautifulsoup4`
* `colorama`

Or install manually:

```bash
pip install requests beautifulsoup4 colorama
```

---

## 🎯 Practice Targets

You can safely test this tool on:

* [http://testphp.vulnweb.com](http://testphp.vulnweb.com)
* [http://demo.testfire.net](http://demo.testfire.net)
* [TryHackMe](https://tryhackme.com/)
* [Hack The Box](https://hackthebox.com/)
* DVWA / Juice Shop / BWAPP / Moodle self-hosted labs

---

## ⚠️ Legal Notice

**This tool is for authorized use only.**

You must have explicit permission to scan and fingerprint any system.
Using ReconX against systems without consent may be illegal.

---

## 👨‍💻 Author

**Iyosiyas Ivasyos**
*Cybersecurity Researcher & Ethical Hacker*
🔗 *GitHub: [github.com/Iyosiprograming](https://github.com/iyosiprograming)*
✉️ *Contact: [iyosieyosiyas@example.com](mailto:iyosieyosiyas@gmail.com)*

---

## 📃 License

Licensed under the **MIT License**.
Free to use, modify, and share — with proper credit to the author.

---

## ⭐️ Contribute

Pull requests welcome. If you have ideas for improvement or want to add advanced fingerprinting logic (like WAF detection, GraphQL exposure, etc.), feel free to fork and contribute.

```


