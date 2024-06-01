import requests
from bs4 import BeautifulSoup
from utils.utils import save_to_csv, save_to_json, print_as_json

def fetch_reuters(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Referer": "https://www.reuters.com/",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    session = requests.Session()
    session.headers.update(headers)
    
    session.get("https://www.reuters.com/")
    
    response = session.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page... CODE: {response.status_code}")

def fetch_bloomberg_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_title = soup.title.string.strip()
        content_div = soup.find('div', class_='body-copy')
        paragraphs = content_div.find_all('p')
        article_text = ' '.join([para.get_text(strip=True) for para in paragraphs])
        return {"title": article_title, "content": article_text}
    else:
        raise Exception(f"failed to fetch the page... CODE: {response.status_code}")

def fetch_cnbc(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_title = soup.title.string.strip()
        content_div = soup.find('div', class_='ArticleBody-articleBody')
        paragraphs = content_div.find_all('p')
        article_text = ' '.join([para.get_text(strip=True) for para in paragraphs])
        return {"title": article_title, "content": article_text}
    else:
        raise Exception(f"Failed to fetch the page... CODE: {response.status_code}")

def fetch_news():
    articles = []
    reuters_urls = [
        "https://www.reuters.com/markets/currencies/dollar-ascendant-surging-us-yields-spur-demand-safe-havens-2024-05-30/",
    ]
    bloomberg_urls = []
    cnbc_urls = []

    for url in reuters_urls:
        try:
            articles.append(fetch_reuters_article(url))
        except Exception as e:
            print(f"Failed to fetch Reuters article: {e}")

    for url in bloomberg_urls:
        try:
            articles.append(fetch_bloomberg_article(url))
        except Exception as e:
            print(f"Failed to fetch Bloomberg article: {e}")

    for url in cnbc_urls:
        try:
            articles.append(fetch_cnbc_article(url))
        except Exception as e:
            print(f"Failed to fetch CNBC article: {e}")

    return articles

# def parse_article_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
    
#     article_title = soup.title.string.strip()
#     print(f"Article Title: {article_title}")
    
#     # Find all divs with the class pattern that contains the paragraphs
#     content_divs = soup.find_all('div', class_='article-body__content__17Yit')

#     paragraphs = []
#     for div in content_divs:
#         for para in div.find_all('div'):
#             paragraphs.append(para.get_text(strip=True))
    
#     # If no paragraphs were found, attempt to find paragraphs in more specific divs
#     if not paragraphs:
#         content_divs = soup.find_all('div', class_='text__text__1FZLe')
#         for div in content_divs:
#             for para in div.find_all('p'):
#                 paragraphs.append(para.get_text(strip=True))
    
#     article_text = ' '.join(paragraphs)
    
#     return {
#         "title": article_title,
#         "content": article_text
#     }

def main():
    url = "https://www.reuters.com/markets/currencies/dollar-ascendant-surging-us-yields-spur-demand-safe-havens-2024-05-30/"
    page_source = fetch_page_source(url)
    article_data = parse_article_content(page_source)

    if article_data:
        save_to_json([article_data], 'data/json/articles.json')
        save_to_csv([article_data], 'data/csv/articles.csv')
        print_as_json([article_data])
    else:
        print("No article content to save")

if __name__ == "__main__":
    main()
