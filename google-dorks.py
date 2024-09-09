import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
import time
import argparse

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


def google_search(query, use_proxy, proxy_url=None):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={query}"

    # List of different User-Agent strings
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/18.18363",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
        "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-G975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
    ]

    headers = {
        "User-Agent": random.choice(user_agents)  # Randomly select a User-Agent
    }

    # Handle proxy if needed
    proxies = None
    if use_proxy and proxy_url:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")
        return None


def extract_urls(html):
    soup = BeautifulSoup(html, 'html.parser')

    urls = []

    # Extract the links from search result divs
    for g in soup.find_all('div', class_='g'):
        link = g.find('a')
        if link and link['href']:
            urls.append(link['href'])

    # Fallback method to handle other potential links
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and "/url?q=" in href:
            actual_url = href.split("/url?q=")[1].split("&")[0]
            urls.append(actual_url)

    return urls


if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Google Dork API Documentation Search Tool. Use this to search for API documentation via Google Dork queries.")
    
    # Add the --target argument
    parser.add_argument('--target', help="The target name for the API documentation search (e.g., Coinbase API Documentation)", required=True)
    
    # Add a flag for using a proxy
    parser.add_argument('--use-proxy', action='store_true', help="Flag to enable proxy usage")
    parser.add_argument('--proxy-url', help="Proxy URL (e.g., http://yourproxyserver:port)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the target from the command-line argument
    target = args.target

    # Determine whether to use a proxy
    use_proxy = args.use_proxy
    proxy_url = args.proxy_url

    # Generate and execute the Google Dork queries
    dorks = generate_google_dorks(target)

    for dork in dorks:
        print(f"\nSearching for: {dork}")
        html = google_search(dork, use_proxy, proxy_url)

        if html:
            urls = extract_urls(html)
            if urls:
                print("Extracted URLs:")
                for url in urls:
                    print(url)
            else:
                print("No URLs found.")
        
        # Add delay of 5 seconds between requests to avoid rate-limiting
        time.sleep(5)  # Wait for 5 seconds between each request
