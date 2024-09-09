# 🚀 Google Dork API Documentation Search Tool

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Google Dork API Documentation Search Tool automates search queries to help you find public API references quickly and efficiently. It allows penetration testers, security researchers, and developers to locate API documentation on popular sites such as GitHub, ReadTheDocs, Swagger, and more using customized Google Dork queries.

---

## 🌟 Features

- **Automated Google Dork Search**: Generate multiple Google Dork queries for API documentation across various websites.
- **Supports Popular Websites**: GitHub, ReadTheDocs, Swagger, Postman, and more.
- **URL Extraction**: Extract relevant URLs directly from Google search results.
- **Lightweight & Efficient**: Minimal dependencies and simple to set up.

---

## 🛠️ Requirements

- **Python 3.7+**
- `requests` library
- `beautifulsoup4` library

To install the required dependencies, run the following command:

```bash
pip install requests beautifulsoup4
```

---

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/google-dork-api-search.git
   cd google-dork-api-search
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧑‍💻 Usage

Run the script and input the target (e.g., "Coinbase API Documentation") when prompted. The script will generate Google Dork queries and extract relevant URLs.

1. **Run the script**:

   ```bash
   python google_dork_search.py
   ```

2. **Input the target**:

   ```bash
   Enter the name of the target (e.g., Coinbase API Documentation): Coinbase
   ```

3. **The script will automatically generate Google Dork queries and extract URLs from the search results.**

### Command-line Example:

You can also pass the target directly via command-line arguments:

```bash
python google_dork_search.py --target "Coinbase API Documentation"
```

---

## 🔍 Example

An example of a Google Dork search for "Coinbase API Documentation":

```bash
Searching for: Coinbase API documentation site:github.com
Extracted URLs:
- https://github.com/coinbase/coinbase-node
- https://github.com/coinbase/coinbase-php

Searching for: Coinbase API documentation site:readthedocs.io
Extracted URLs:
- https://coinbase.readthedocs.io/en/latest/
...
```

---

## 📂 Project Repository

You can find the source code and report issues at the official GitHub repository:

[GitHub Repository](https://github.com/MeltDown23/Google-Droks)

---

