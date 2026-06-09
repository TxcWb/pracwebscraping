# Practice Web Scraping

A Python web scraper that extracts book information from [books.toscrape.com](https://books.toscrape.com/), including titles, prices, and availability status. The scraped data is saved to a CSV file for further analysis.

## Overview

This project demonstrates practical web scraping techniques using Python. It scrapes a multi-page website, handles pagination, and exports the collected data into a structured CSV format.

## Features

- **Multi-page scraping**: Automatically follows pagination links to scrape all pages
- **Data extraction**: Collects book titles, prices, and availability information
- **CSV export**: Saves data to `books.csv` for easy analysis
- **Error handling**: Gracefully handles network errors and exceptions
- **Rate limiting**: Includes polite delays between requests (0.5 seconds)
- **Character encoding**: Properly handles UTF-8 encoding

## Project Structure

```
pracwebscraping/
├── README.md          # Project documentation
├── scraper.py         # Main web scraper script
└── books.csv          # Output file with scraped book data
```

## Requirements

- Python 3.6+
- `requests` - HTTP library for fetching web pages
- `beautifulsoup4` - HTML/XML parsing library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TxcWb/pracwebscraping.git
cd pracwebscraping
```

2. Install dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper:
```bash
python scraper.py
```

The script will:
1. Start scraping from `https://books.toscrape.com/index.html`
2. Parse each page to extract book information
3. Follow pagination links automatically
4. Display progress messages for each page
5. Save all collected books to `books.csv`
6. Display the total number of books found

### Output

The `books.csv` file will contain three columns:
- **title**: The book title
- **price**: The book price (including currency symbol)
- **availability**: Stock availability status

## How It Works

The scraper uses BeautifulSoup to parse HTML and locate:
- Product information in `<article class="product_pod">` elements
- Book titles in `<h3>` → `<a>` tags
- Prices in `<p class="price_color">` elements
- Availability in `<p class="instock availability">` elements
- Next page links in `<li class="next">` elements

It implements proper URL resolution using `urljoin()` to handle relative links and includes rate limiting (0.5-second delay between requests) to be respectful to the server.

## Example Output

```csv
title,price,availability
A Light in the Attic,£51.77,In stock
Tipping the Velvet,£53.74,In stock
Soumission,£50.10,In stock
...
```

## Learning Outcomes

This project teaches:
- HTTP requests and response handling
- HTML parsing with BeautifulSoup
- CSS selector usage for data extraction
- Pagination handling
- CSV file writing
- Exception handling for network errors
- Web scraping best practices (rate limiting, polite delays)

## License

This project is provided as-is for educational purposes.

## Notes

- The target website (books.toscrape.com) is specifically designed for web scraping practice
- Always check a website's `robots.txt` and terms of service before scraping
- The 0.5-second delay between requests is a courtesy to avoid overloading servers
