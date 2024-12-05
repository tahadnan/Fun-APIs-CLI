import os
import json
from json.decoder import JSONDecodeError
from typing import Literal
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from ..constants import CONFIG_FILE_PATH, console
from ..utils import error_handler

def save_api_key(api_key: str , which_api_key : Literal["ninjas_api_key", "superhero_api_key"]) -> None:
    if which_api_key.strip() not in ["ninjas_api_key", "superhero_api_key"]:
        console.print(f"[red]Invalid API choice: '{which_api_key}'. Please check the documentation for valid and needed API keys.[/red]")
        return 
    try:
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH,'r') as config_file:
                config = json.load(config_file)
        else:
            config = {"api_keys": {}}

        config["api_keys"][which_api_key] = api_key  

        with open(CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(config, config_file, indent=4)
        console.print(f"[green]{which_api_key} key succesfully saved to \"{CONFIG_FILE_PATH}\"[/green]")
    except JSONDecodeError:
        console.print("[red]Error reading JSON file. Creating a new one...[/red]")
        config = {"api_keys": {which_api_key: api_key}}
        with open(CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(config, config_file, indent=4)

def input_api_key(which_api_key : Literal["ninjas_api_key", "superhero_api_key"]) -> str:
    if which_api_key.lower().strip() not in ["ninjas_api_key", "superhero_api_key"]:
        console.print(f"[red]Invalid API choice: '{which_api_key}'. Please check the documentation for valid and needed API keys.[/red]")
        return     
    api_key = prompt(f"Enter your {which_api_key}: ", is_password=True).strip()
    if not api_key:
        console.print(f"[red]Input field cannot be empty. Exiting...[/red]")
        exit(1)
    return api_key

def configure_api_key(which_api_key : Literal["ninjas_api_key", "superhero_api_key"]) -> str:
    if which_api_key.lower().strip() not in ["ninjas_api_key", "superhero_api_key"]:
        console.print(f"[red]Invalid API choice: '{which_api_key}'. Please check the documentation for valid and needed API keys.[/red]")
        return 
    api_key = input_api_key(which_api_key)
    if not api_key:
        return 
    save_api_key(api_key,which_api_key)
    return api_key

def load_api_key(which_api_key : Literal["ninjas_api_key", "superhero_api_key"]) -> str:
    if which_api_key.lower().strip() not in ["ninjas_api_key", "superhero_api_key"]:
        console.print(f"[red]Invalid API choice: '{which_api_key}'. Please check the documentation for valid and needed API keys.[/red]")
        return 
    try:
        if not os.path.exists(CONFIG_FILE_PATH):
            console.print("[yellow]Config file not found. Creating a new one...[/yellow]")
            api_key = input_api_key(which_api_key)
            save_api_key(api_key, which_api_key)

        with open(CONFIG_FILE_PATH, 'r') as config_file:
            config = json.load(config_file)
            api_key = config.get("api_keys", {}).get(which_api_key, '').strip()

        if not api_key:
            console.print("[red]No API key found in config.json.[/red]")
            return configure_api_key(which_api_key)
        return api_key
    except JSONDecodeError:
        console.print("[red]Broken JSON file")
        try:
            retry = confirm("Do you want to input a new API key?")
            if retry:
                return configure_api_key()
            else:
                console.print("[magenta]Have a good day!")
                exit(1)
        except (EOFError, KeyboardInterrupt):
            print("Exiting...")
            exit(1)

        



