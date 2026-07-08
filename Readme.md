# 🌐 Web Scraper - Intelligent Quotes Scraping Tool

<div align="center">






### 🚀 A robust Python web scraper that intelligently crawls multiple pages, extracts quotes, and exports structured data in JSON format.

</div>

---

# 📖 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Usage](#-usage)
* [How It Works](#-how-it-works)
* [Example Output](#-example-output)
* [Technologies Used](#-technologies-used)
* [Configuration](#-configuration)
* [Future Improvements](#-future-improvements)
* [Learning Outcomes](#-learning-outcomes)
* [Author](#-author)
* [License](#-license)

---

# 📌 Overview

This project is a **Python-based web scraper** built using **Requests** and **BeautifulSoup**.

It automatically:

* 🌍 Connects to a website
* 📄 Crawls through multiple pages
* 📝 Extracts quote text, author names, and tags
* 🔁 Follows pagination automatically
* 💾 Saves the scraped data into a structured JSON file
* ⚡ Includes retry mechanisms and logging for reliability

The scraper is primarily designed for educational purposes using the **Quotes to Scrape** website, but the code can easily be adapted for similar websites.

---

# ✨ Features

✅ Automatic multi-page crawling

✅ Intelligent pagination detection

✅ BeautifulSoup HTML parsing

✅ Clean and modular code structure

✅ Dataclass-based data storage

✅ Automatic retry mechanism

✅ Request timeout handling

✅ Logging support

✅ JSON export

✅ Easily customizable

---

# 📂 Project Structure

```
Web_Scraper/
│
├── Web_Scraper.py        # Main scraper
├── quotes.json           # Generated output
└── README.md
```

---

# ⚙ Installation

## Clone the repository

```bash
git clone https://github.com/Swapnil1105-arc/Web_Scraper.git

cd Web_Scraper
```

## Install dependencies

```bash
pip install requests beautifulsoup4 lxml
```

Or

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

Run the program:

```bash
python Web_Scraper.py
```

You'll be prompted to enter a website URL:

```
Enter the base URL of the quotes website:

http://quotes.toscrape.com
```

The scraper will automatically visit every page until no additional pages remain.

---

# ⚙ How It Works

```text
Start URL
     │
     ▼
Fetch HTML Page
     │
     ▼
Parse Quotes
     │
     ▼
Extract:
• Quote
• Author
• Tags
     │
     ▼
Find Next Page
     │
     ▼
Repeat Until Last Page
     │
     ▼
Export JSON
```

---

# 📊 Example Output

```json
[
  {
    "text": "The world as we have created it is a process of our thinking.",
    "author": "Albert Einstein",
    "tags": "change, deep-thoughts, thinking"
  },
  {
    "text": "It is our choices...",
    "author": "J.K. Rowling",
    "tags": "abilities, choices"
  }
]
```

---

# 🛠 Technologies Used

| Technology    | Purpose                |
| ------------- | ---------------------- |
| Python        | Programming Language   |
| Requests      | HTTP Requests          |
| BeautifulSoup | HTML Parsing           |
| lxml          | Fast HTML Parser       |
| JSON          | Data Storage           |
| Logging       | Debugging & Monitoring |
| Dataclasses   | Structured Data        |

---

# ⚙ Configuration

You can customize these settings inside the script:

```python
REQUEST_DELAY = 1.0
TIMEOUT = 10
MAX_RETRIES = 3
```

These parameters help avoid excessive requests and improve scraper reliability.

---

# 🎯 Learning Outcomes

This project demonstrates:

* HTTP requests
* HTML parsing
* CSS Selectors
* Pagination scraping
* Exception handling
* Logging
* Retry logic
* Dataclasses
* JSON serialization
* Clean Python project organization

---

# 🚀 Future Improvements

* [ ] CSV Export
* [ ] Excel Export
* [ ] Command-line arguments
* [ ] Async scraping
* [ ] Progress bar
* [ ] Database storage (SQLite/MySQL)
* [ ] Image downloading
* [ ] Proxy support
* [ ] User-agent rotation
* [ ] Docker support

---

# 👨‍💻 Author

**Swapnil Gupta**

GitHub:

**https://github.com/Swapnil1105-arc**

If you found this project helpful, don't forget to ⭐ the repository!

---

# 📜 License

This project is intended for **educational and learning purposes**.

Please respect website Terms of Service and robots.txt when scraping publicly available websites.

---

<div align="center">

### ⭐ If you enjoyed this project, consider giving it a Star!

**Happy Coding! 🚀**

</div>

