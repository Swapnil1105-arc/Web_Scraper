# Level 3 Task 1

from __future__ import annotations
import csv
import json
import time
import logging
from dataclasses import dataclass, asdict


import requests
from bs4 import BeautifulSoup



print("-"*45)
print("         DATA VISUALIZATION TOOL")
print("-"*45)



logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = input("Enter the base URL of the quotes website (e.g., http://quotes.toscrape.com): ").strip()
HEADERS = {
   
    "User-Agent": "Mozilla/5.0 (educational-scraper; +https://example.com/bot-info)"
}
REQUEST_DELAY = 1.0   
TIMEOUT = 10           
MAX_RETRIES = 3


@dataclass
class Quote:
    text: str
    author: str
    tags: str  

def fetch_page(url: str) -> BeautifulSoup | None:
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()  
            return BeautifulSoup(response.text, "lxml")
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt}/{MAX_RETRIES} failed for {url}: {e}")
            time.sleep(2 * attempt)  
    logger.error(f"Giving up on {url} after {MAX_RETRIES} attempts.")
    return None


def parse_quotes(soup: BeautifulSoup) -> list[Quote]:
    quotes = []
    for block in soup.select("div.quote"):
        text_tag = block.select_one("span.text")
        author_tag = block.select_one("small.author")
        tag_elements = block.select("div.tags a.tag")

        text = text_tag.get_text(strip=True) if text_tag else ""
        author = author_tag.get_text(strip=True) if author_tag else ""
        tags = ", ".join(t.get_text(strip=True) for t in tag_elements)

        quotes.append(Quote(text=text, author=author, tags=tags))
    return quotes


def get_next_page_url(soup: BeautifulSoup, current_url: str) -> str | None:
    next_link = soup.select_one("li.next a")
    if next_link and next_link.get("href"):
        return requests.compat.urljoin(current_url, next_link["href"])
    return None


def scrape_all_pages(start_url: str) -> list[Quote]:
    all_quotes: list[Quote] = []
    url = start_url
    page_num = 1

    while url:
        logger.info(f"Scraping page {page_num}: {url}")
        soup = fetch_page(url)
        if soup is None:
            break

        page_quotes = parse_quotes(soup)
        logger.info(f"  -> found {len(page_quotes)} quotes")
        all_quotes.extend(page_quotes)

        url = get_next_page_url(soup, url)
        page_num += 1
        time.sleep(REQUEST_DELAY)  

    return all_quotes


def save_to_csv(quotes: list[Quote], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        for q in quotes:
            writer.writerow(asdict(q))
    logger.info(f"Saved {len(quotes)} quotes to {filename}")


def save_to_json(quotes: list[Quote], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([asdict(q) for q in quotes], f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(quotes)} quotes to {filename}")


if __name__ == "__main__":
    quotes = scrape_all_pages(BASE_URL)
    save_to_json(quotes, "quotes.json")

    print(f"\nTotal quotes scraped: {len(quotes)}")
    