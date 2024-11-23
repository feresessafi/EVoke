import os
from openai import AzureOpenAI
import json
from rich.console import Console
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

console = Console()

class ArticleSummarizer:
    def __init__(self):
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        
        if not api_key or not endpoint:
            raise ValueError(
                "Missing Azure OpenAI credentials. Please ensure AZURE_OPENAI_API_KEY and "
                "AZURE_OPENAI_ENDPOINT are set in your .env file"
            )
            
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version="2024-08-01-preview",
            azure_endpoint=endpoint
        )

    def create_combined_article(self, story_group: Dict) -> Dict:
        """Create one comprehensive article from multiple sources"""
        
        # Collect all articles in the group
        articles = story_group['articles']
        
        # Create context from all articles
        sources = []
        for idx, article in enumerate(articles, 1):
            sources.append(f"""
Quelle {idx}: {article['title']}
{article['content']}
""")
        
        prompt = f"""Als Journalist sollst du einen umfassenden Artikel über folgendes Thema schreiben:
{story_group['story_title']}

Nutze dafür diese Quellen:
{''.join(sources)}

Erstelle einen gut strukturierten Artikel mit:
1. Einer packenden Überschrift
2. Einem kurzen Einleitungsabsatz (Lead)
3. Dem Hauptteil mit allen wichtigen Details
4. Quellenangaben am Ende

Der Artikel soll alle wichtigen Informationen aus den Quellen zusammenfassen und in einen klaren Kontext setzen.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du bist ein erfahrener Wirtschaftsjournalist."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            combined_article = {
                'story_id': story_group.get('story_id', 'unknown'),
                'story_title': story_group['story_title'],
                'main_entity': story_group['main_entity'],
                'article_text': response.choices[0].message.content,
                'source_count': len(articles),
                'sources': [a['url'] for a in articles]
            }
            
            console.log(f"[green]✓ Created combined article for:[/green] {story_group['story_title']}")
            return combined_article
            
        except Exception as e:
            console.log(f"[red]Error creating combined article: {str(e)}[/red]")
            return None

def main():
    # Load classified articles
    console.log("Loading classified articles...")
    with open('classified_articles.json', 'r', encoding='utf-8') as f:
        classified = json.load(f)
    
    summarizer = ArticleSummarizer()
    combined_articles = []
    
    # Process each story group
    for story_id, story_group in classified.items():
        console.log(f"\nProcessing story group: {story_group['story_title']}")
        combined = summarizer.create_combined_article(story_group)
        if combined:
            combined_articles.append(combined)
    
    # Save combined articles
    with open('combined_articles.json', 'w', encoding='utf-8') as f:
        json.dump(combined_articles, f, ensure_ascii=False, indent=4)
    
    console.log(f"\n[bold green]Created {len(combined_articles)} combined articles[/bold green]")

if __name__ == "__main__":
    main()