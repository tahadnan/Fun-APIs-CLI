import requests
from requests import ConnectionError
from pprint import pprint
from typing import List, Dict
from rich.console import Console
from rich import print_json
console = Console()

def fetch_animal_info(name : str) -> List[Dict]:
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'yCznsy0vc3u7k2r8U9RrLQ==LiWWdUaMMfVAiTb6'})
        if response.status_code == requests.codes.ok:
            if response.json():
                return response.json()
            else:
                console.print(f"[red]No animals found matching '{name}'.")
                return []
        else:
            console.print(f"[red]Error: {response.status_code} {response.text}")
            return []
    except ConnectionError:
        console.print("[red]No internet connection! Please check your network and try again.[/red]")
        return None

def display_animal_info(animals_data: List[Dict]):
    if not animals_data:
        return 

    for data_dict in animals_data:
        console.print("[green]\n=== Animal Information ===")
        
        console.print(f"[red]\nName:[/red] {data_dict['name']}")
        
        console.print("[cyan]\nTaxonomy:")
        for key, value in data_dict['taxonomy'].items():
            console.print(f"  [cyan i]{key.title().replace("_"," ")}:[/cyan i] {value}")
        
        console.print("[yellow]\nLocations:", ", ".join(data_dict['locations']))
        
        console.print("[blue]\nCharacteristics:")
        for key, value in data_dict['characteristics'].items():
            formatted_key = key.replace('_', ' ').title()
            console.print(f"   [red i]{formatted_key}:[/red i] {value}")

def animal(animal_name : str = None) -> None:
    if not animal_name:
        console.print("[yellow] Please provide an animal name.")
        return
    with console.status("Looking around...", spinner="monkey"):
        display_animal_info(fetch_animal_info(name=animal_name))

