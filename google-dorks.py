import requests
from bs4 import BeautifulSoup
import urllib.parse

print("This tool is only for PrimeSec PT Team.")
def generate_google_dorks(target):
    sites = [
        "site:github.com",
        "site:readthedocs.io",
        "site:developer.coinbase.com",
        "site:swagger.io",
        "site:postman.com",
        "site:apidocs.io",
        "site:medium.com",
        "site:stackoverflow.com",
        "site:dev.to",
        "site:reddit.com",
    ]

    queries = [
        f"{target} API documentation",
        f"{target} API reference",
        f"{target} REST API documentation",
        f"{target} GraphQL API documentation",
        f"{target} public API documentation",
        f"{target} developer API docs",
        f"{target} API integration guide",
    ]

    dorks = []
    for site in sites:
        for query in queries:
            dorks.append(f"{query} {site}")
    return dorks


def google_search(query):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")
        return None


def extract_urls(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Updated logic to extract URLs
    urls = []

    for g in soup.find_all('div', class_='g'):
        link = g.find('a')
        if link and link['href']:
            urls.append(link['href'])

    # Fallback method in case the above misses URLs
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and "/url?q=" in href:
            actual_url = href.split("/url?q=")[1].split("&")[0]
            urls.append(actual_url)

    return urls


if __name__ == "__main__":
    target = input("Enter the name of the target (e.g., Coinbase API Documentation): ")
    dorks = generate_google_dorks(target)

    for dork in dorks:
        print(f"\nSearching for: {dork}")
        html = google_search(dork)

        if html:
            urls = extract_urls(html)
            if urls:
                print("Extracted URLs:")
                for url in urls:
                    print(url)
            else:
                print("No URLs found.")
