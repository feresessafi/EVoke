import json
import os
from openai import AzureOpenAI
from typing import List, Dict
import time
from rich.console import Console

console = Console()

class ArticleClassifier:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-08-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def classify_article(self, article: Dict) -> Dict:
        """Classify a single article using Azure OpenAI"""
        prompt = f"""Analysiere diesen deutschen Nachrichtenartikel und gruppiere ihn:

Titel: {article['title']}
Inhalt: {article['content']}

Antworte NUR im folgenden JSON Format:
{{
    "category": "EINE der folgenden Kategorien: E-Mobilität, Batterietechnologie, Autoindustrie, Infrastruktur, Wirtschaft, Politik",
    "keywords": ["2-3 wichtige Schlüsselwörter"],
    "companies": ["erwähnte Firmen"],
    "summary": "2-3 Sätze Zusammenfassung"
}}"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du bist ein Experte für die Analyse von Nachrichtenartikeln."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500,
                response_format={ "type": "json_object" }
            )
            
            classification = json.loads(response.choices[0].message.content)
            article.update(classification)
            console.log(f"[green]✓ Classified:[/green] {article['title'][:100]}")
            return article
            
        except Exception as e:
            console.log(f"[red]Error classifying article: {str(e)}[/red]")
            console.log(f"Response content: {response.choices[0].message.content if 'response' in locals() else 'No response'}")
            return article

    def process_articles(self, articles: List[Dict]) -> Dict:
        """Process all articles and group them"""
        console.log(f"Processing {len(articles)} articles...")
        
        classified_articles = []
        for article in articles:
            classified = self.classify_article(article)
            classified_articles.append(classified)
            time.sleep(1)  # Rate limiting

        # Group by category
        grouped = {}
        for article in classified_articles:
            category = article.get('category', 'Unknown')
            if category not in grouped:
                grouped[category] = []
            grouped[category].append(article)

        return grouped

def main():
    # Load articles
    with open('cleaned_articles.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)

    classifier = ArticleClassifier()
    grouped_articles = classifier.process_articles(articles)

    # Save results
    with open('classified_articles.json', 'w', encoding='utf-8') as f:
        json.dump(grouped_articles, f, ensure_ascii=False, indent=4)

    # Print summary
    console.rule("[bold]Classification Summary[/bold]")
    for category, articles in grouped_articles.items():
        console.log(f"{category}: {len(articles)} articles")

if __name__ == "__main__":
    main()
