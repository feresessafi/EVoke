import feedparser
import requests
from bs4 import BeautifulSoup
import json
import re

def fetch_rss_links(rss_url):
    """Fetch and parse RSS feed."""
    feed = feedparser.parse(rss_url)
    links = [entry.link for entry in feed.entries]
    return links

def is_valid_article(url):
    """Check if the URL is accessible and not behind a paywall."""
    try:
        response = requests.get(url, timeout=10)
                
        # Check if the status code is OK and the page doesn't contain paywall markers
        if response.status_code == 200 and 'paywall' not in response.text.lower() and 'offer' not in response.text.lower():
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def clean_article_content(article_content):
    """Clean the article content by removing unwanted text like ads and navigation."""
    soup = BeautifulSoup(article_content, 'html.parser')
    
    # Remove common unwanted elements
    for unwanted_tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
        unwanted_tag.decompose()
    
    # Get the text content
    cleaned_text = soup.get_text()
    
    # Remove common unwanted text patterns
    patterns_to_remove = [
        # Headers and Navigation
        r'AUTO BILD Logo.*?KreuzSuche',
        r'Direkt zum Inhalt.*?wechseln',
        r'HomeMobilität.*?Loading\.\.\.', 
        r'Schlagzeilen.*?Loading\.\.\.', 
        
        # Footer and Service Links
        r'Service-Links.*?Test',
        r'Der NDR.*?Rundfunk$',
        r'Themen:.*?OK$',
        r'Dieses Thema im Programm:.*$',
        r'Beitrag teilen.*$',
        r'Dieser Artikel wurde ausgedruckt unter der Adresse:.*$',
        r'Mehr Nachrichten aus.*$',
        
        # Social Media and Sharing
        r'ANZEIGE.*?vergleichen\*',
        r'Artikel teilen:.*?Archivbild$',
        r'Feedback an die Redaktion.*$',
        
        # Media Elements
        r'Play.*?Test',
        r'Alle \w+ Videos',
        r'AUDIO:.*?\d+ Min\)',
        r'Foto:.*$',
        
        # Advertisements and Promotions
        r'\* Die durchschnittliche Ersparnis.*?Händler\.',
        r'Zum Angebot.*?Deal',
        r'Ein Service von.*?Modell',
        r'Anzeige:.*$',
        
        # Metadata and Timestamps
        r'Aktualisiert am.*?Uhr',
        r'©.*$',
        r'Lesedauer:.*?Min\.',
        
        # Navigation Elements
        r'News folgen.*$',
        r'Weitere Informationen.*?mehr$',
        r'Videos.*?Min$',
        
        # URLs and Links
        r'https?://\S+',
        
        # Repeated Headers
        r'^.*?\| NDR\.de - Nachrichten.*?Direkt zum Inhalt',
    ]
    
    for pattern in patterns_to_remove:
        cleaned_text = re.sub(pattern, '', cleaned_text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove excess whitespace and normalize
    cleaned_text = ' '.join(cleaned_text.split())
    
    # Remove any remaining common prefixes
    prefixes_to_remove = [
        r'^AUTO BILD\s*-\s*',
        r'^von [A-Za-z\s]+\s*',  # Removes author attribution at start
    ]
    
    for prefix in prefixes_to_remove:
        cleaned_text = re.sub(prefix, '', cleaned_text)
    
    return cleaned_text

def fetch_and_clean_articles(links):
    """Fetch and clean the articles, return as a list of dictionaries."""
    articles = []
    
    # Get the RSS feed entries to match titles with URLs
    feed = feedparser.parse(rss_url)
    url_to_title = {entry.link: entry.title for entry in feed.entries}
    
    for url in links:
        if is_valid_article(url):
            try:
                response = requests.get(url, timeout=10)
                response.encoding = 'utf-8'  # Ensure UTF-8 encoding handling
                cleaned_content = clean_article_content(response.text)
                cleaned_content_decoded = cleaned_content
                articles.append({
                    'url': url,
                    'title': url_to_title.get(url, ''),  # Get title from RSS feed
                    'content': cleaned_content_decoded
                })
            except requests.exceptions.RequestException:
                continue  # Skip if there is an error fetching the article
    
    return articles

def save_articles_as_json(articles, output_file):
    """Save articles to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)  # Ensure UTF-8 encoding in the output

# Example usage:
#rss_url = 'https://www.autobild.de/rss/22590661.xml'  # Replace with your RSS feed URL
rss_url = 'https://rss.app/feeds/MLuDKqkwFtd2tuMr.xml'
output_file = 'cleaned_articles.json'

# Step 1: Fetch article links from RSS
links = fetch_rss_links(rss_url)

# Step 2: Fetch and clean the valid articles
valid_articles = fetch_and_clean_articles(links)

# Step 3: Save cleaned articles to JSON
save_articles_as_json(valid_articles, output_file)

print(f"Saved {len(valid_articles)} valid articles to {output_file}.")