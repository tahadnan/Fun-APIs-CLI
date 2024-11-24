import requests
from requests import ConnectionError
import random
from typing import Union, List, TypedDict, Optional
from rich.console import Console
console = Console()

class Quote(TypedDict):
    quote : str
    author : str
    category : str

categories   = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday", "business", "car", "change", "communication", "computers", "cool", "courage", "dad", "dating", "death", "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith", "family", "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future", "god", "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope", "humor", "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning", "legal", "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"]

categories_noun = {
    "alone": "loneliness",
    "amazing": "amazement",
    "best": "excellence",
    "cool": "coolness",
    "famous": "fame",
    "funny": "humor",
    "good": "goodness",
    "great": "greatness",
    "inspirational": "inspiration",
    "legal": "legality",
    "medical": "medicine",
}

def fetch_quote(category : Optional[str] = None) -> Union[List[Quote], int]:
    if not category:
        category = random.choice(categories)
    else:
        category = {v: k for k, v in categories_noun.items()}.get(category.lower(), category.lower())
        if category not in categories:
            console.print(f"[red]Invalid category '{category}'. Falling back to random choice![/red]")
            category = random.choice(categories)
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'yCznsy0vc3u7k2r8U9RrLQ==LiWWdUaMMfVAiTb6'})
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            console.print(f"[red]Error: {response.status_code} {response.text}")
            return 0
    except ConnectionError:
        console.print("[red]No internet connection! Please check your network and try again.[/red]")
    return 0

def display_quote(quote : Union[List[Quote], int]) -> None:
    if quote == 0:
        return 
    quote = quote[0]
    topic = categories_noun.get(quote['category'],quote['category']).capitalize()
    console.print(f'''
    [green bold]"{quote['quote']}"[/green bold]
    said by [cyan i]{quote['author']}[/cyan i] about [red]{topic}[/red]
    ''')

def quote(category : Optional[str] = None) -> None:
    with console.status("Fetching a quote...", spinner="earth"):
        display_quote(quote=fetch_quote(category))

if __name__ == "__main__":
    quote()