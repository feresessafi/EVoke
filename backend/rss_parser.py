import feedparser as fp
import requests
import json
from bs4 import BeautifulSoup

def check_url_access(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        elif response.status_code in [403, 404]:
            return False
        elif response.status_code == 302:
            return "redirected"
    except requests.RequestException:
        return False

def is_paywalled(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        keywords = ["subscribe", "paywall", "premium", "login", "register", "unlimited", "access", "membership", "premium", "exclusive", "content", "subscription", "sign in", "sign up", "sign-in", "sign-up", "log in", "log-in", "register", "join", "account", "pay"]
        return any(keyword in soup.get_text().lower() for keyword in keywords)
    except requests.RequestException:
        return False

def requires_login(url):
    try:
        response = requests.get(url, timeout=5)
        return "login" in response.url.lower()
    except requests.RequestException:
        return False

feeds = [
    "https://rss.app/feeds/MLuDKqkwFtd2tuMr.xml",
    # "https://www.autobild.de/rss/22590661.xml",
    # "https://rss.app/feed/AY3gpY8fWOkfCCWR"
]


count_not_accessible = 0

articles = {}

for feed in feeds:
    parsed_feed = fp.parse(feed)
    print("Parsed feed {} has {} entries".format(feed, len(parsed_feed.entries)))
    for entry in parsed_feed.entries:
        url = entry.link
        # print("Checking URL: {}".format(url))
        if check_url_access(url) and not is_paywalled(url) and not requires_login(url):
            # print("URL is accessible")
            # open the URL and extract the article text
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            article_text = " ".join([p.get_text() for p in paragraphs])
            articles[url] = {
                "article_title": entry.title,
                "article_text": article_text
            }
            continue
        else:
            print("URL {} is not accessible\n".format(url))
            count_not_accessible += 1
            
print("Total number of inaccessible URLs: {}".format(count_not_accessible))
with open("articles.json", "w") as f:
    json.dump(articles, f, indent=4)