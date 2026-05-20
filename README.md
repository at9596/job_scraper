# Job Scraper CLI

A simple job scraper built with Python.

This project helps learn:
- Web scraping
- HTTP requests
- HTML parsing
- Modular Python structure

---

# Features

- Fetch job listings from website
- Extract:
  - Job title
  - Company
  - Location
- Clean modular structure

---

# Project Structure

```bash
job_scraper/
│
├── app/
│   ├── main.py
│   │
│   ├── scrapers/
│   │   └── job_scraper.py
│   │
│   └── parsers/
│       └── parser.py
│
├── requirements.txt
├── README.md
└── run.py
```

---

# Requirements

- Python 3.8+

---

# requirements.txt

```txt
beautifulsoup4==4.13.4
requests==2.32.3
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

# Usage

Run scraper:

```bash
python3 run.py
```

---

# Example Output

```bash
------------------------
Title    : Python Developer
Company  : ABC Company
Location : Remote
```