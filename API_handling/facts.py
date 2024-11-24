import requests
from requests import ConnectionError
from typing import List, TypedDict, Optional
from rich.console import Console
console = Console()

class Fact(TypedDict):
    fact: str

def fetch_fact() -> Optional[List[Fact]]:
    api_url = 'https://api.api-ninjas.com/v1/facts'
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'yCznsy0vc3u7k2r8U9RrLQ==LiWWdUaMMfVAiTb6'})
        if response.status_code == requests.codes.ok:
            fact = response.json()
            if isinstance(fact, list) and len(fact) > 0:
                return fact
            console.print("[yellow]No facts received from the API!")
        else:
            console.print(f"[red]Error: {response.status_code} {response.text}")
    except ConnectionError:
        console.print("[red]No internet connection! Please check your network and try again.[/red]")
        return None

def display_fact(fact: Optional[List[Fact]]) -> None:
    if not fact:
        console.print("[yellow] No facts to display!")
        return
    console.print(f"[green bold]Fun Fact:[/green bold] {fact[0]['fact']}")

def fact() -> None:
    with console.status("Fetching a fun fact...", spinner="earth"):
        display_fact(fetch_fact())
