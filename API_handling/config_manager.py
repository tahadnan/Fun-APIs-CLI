import json
from json.decoder import JSONDecodeError
import os
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from .constants import CONFIG_PATH, console

def save_api_key(api_key: str) -> None:
    with open(CONFIG_PATH, 'w') as file:
        json.dump({'api_key': api_key}, file, indent=4)
    console.print(f"[green]API key succesfully saved to \"{CONFIG_PATH}\"[/green]")

def input_api_key() -> str:
    api_key = prompt("Enter your API key: ", is_password=True).strip()
    if not api_key:
        console.print("[red]API key cannot be empty. Exiting...[/red]")
        exit(1)
    return api_key

def load_api_key() -> str:
    try:
        if not os.path.exists(CONFIG_PATH):
            console.print("[yellow]Config file not found. Creating a new one...[/yellow]")
            api_key = input_api_key()
            save_api_key(api_key)

        with open(CONFIG_PATH, 'r') as file:
            config = json.load(file)
            api_key = config.get('api_key', '').strip()

        if not api_key:
            console.print("[red]No API key found in config.json.[/red]")
            api_key = input_api_key()
            save_api_key(api_key)
        return api_key
    except JSONDecodeError:
        console.print("[red]Broken JSON file")
        retry = confirm("Do you want to input a new API key?")
        if retry:
            return configure_api_key()
        else:
            console.print("[magenta]Have a good day!")
            exit(1)


def configure_api_key() -> str:
    api_key = input_api_key()
    if not api_key:
        return 
    save_api_key(api_key)
    return api_key


