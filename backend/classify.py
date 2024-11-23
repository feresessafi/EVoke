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
        prompt = f"""Analysiere diesen deutschen Nachrichtenartikel und identifiziere die Hauptgeschichte:

Titel: {article['title']}
Inhalt: {article['content']}

Antworte NUR im folgenden JSON Format:
{{
    "story_id": "Kurzer eindeutiger Identifier für die Geschichte (z.B. 'northvolt_insolvenz', 'hamburg_ladestationen')",
    "story_title": "Ein kurzer Titel der die Hauptgeschichte beschreibt",
    "main_entity": "Hauptakteur der Geschichte (z.B. Firma oder Institution)",
    "keywords": ["2-3 wichtige Schlüsselwörter"],
    "summary": "2-3 Sätze Zusammenfassung"
}}"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du bist ein Experte für das Gruppieren ähnlicher Nachrichten."},
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
            return article

    def process_articles(self, articles: List[Dict]) -> Dict:
        """Process all articles and group them by story"""
        console.log(f"Processing {len(articles)} articles...")
        
        classified_articles = []
        for article in articles:
            classified = self.classify_article(article)
            classified_articles.append(classified)
            time.sleep(1)

        # Group by story_id
        grouped = {}
        for article in classified_articles:
            story_id = article.get('story_id', 'unknown')
            if story_id not in grouped:
                grouped[story_id] = {
                    'story_title': article.get('story_title', ''),
                    'main_entity': article.get('main_entity', ''),
                    'articles': []
                }
            grouped[story_id]['articles'].append(article)

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
    for story_id, data in grouped_articles.items():
        console.log(f"Story ID: {story_id}")
        console.log(f"Story Title: {data['story_title']}")
        console.log(f"Main Entity: {data['main_entity']}")
        console.log(f"Articles: {len(data['articles'])}")

if __name__ == "__main__":
    main()
