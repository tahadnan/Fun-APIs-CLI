import os
import json
from json.decoder import JSONDecodeError
from typing import Literal
from prompt_toolkit import prompt, HTML
from prompt_toolkit.shortcuts import confirm
from rich.prompt import Prompt
from constants import CONFIG_FILE_PATH, console, valid_apis_keys
from utils import cli_errors

def verify_api_key_legibility(api_key : str) -> None:
    if api_key.lower().strip() not in valid_apis_keys:
        console.print(f"[red]Invalid API choice: '{ api_key}'. Please check the documentation for valid and needed API keys.[/red]")
        return 

def save_api_key(api_key: str , which_api_key : Literal[valid_apis_keys]) -> None:
    verify_api_key_legibility(which_api_key)
    try:
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH,'r') as config_file:
                config = json.load(config_file)
        else:
            config = {"api_keys": {}}

        config["api_keys"][which_api_key] = api_key  

        with open(CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(config, config_file, indent=4)
        console.print(f"[green]{which_api_key} key successfully saved to \"{CONFIG_FILE_PATH}\"[/green]")
    except JSONDecodeError:
        console.print("[red]Error reading JSON file. Creating a new one...[/red]")
        config = {"api_keys": {which_api_key: api_key}}
        with open(CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(config, config_file, indent=4)

def input_api_key(which_api_key : Literal[valid_apis_keys]) -> str:
    verify_api_key_legibility(which_api_key)    
    api_key = prompt(f"Enter your {which_api_key}: ", is_password=True).strip()
    if not api_key:
        console.print(f"[red]Input field cannot be empty. Exiting...[/red]")
        exit(1)
    return api_key

@cli_errors
def configure_api_key() -> str:
    valid_apis_keys_string : str = f"{"; ".join(valid_apis_keys)}"
    console.print(f"Which API key are you willing to configure [bright_blue i]({valid_apis_keys_string})[/bright_blue i]")
    while True:
        which_api_key = prompt(HTML(f"> "))
        if which_api_key in valid_apis_keys:
            break
        else:
            console.print(f"{which_api_key} [red i] is invalid Please choose a valid option.")
            console.print(f"Available options => [bright_blue i]({valid_apis_keys_string})[/bright_blue i]")
            continue
    api_key = input_api_key(which_api_key)
    if not api_key:
        return 
    save_api_key(api_key,which_api_key)
    return api_key
@cli_errors
def load_api_key(which_api_key : Literal[valid_apis_keys]) -> str:
    verify_api_key_legibility(which_api_key)
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
        retry = confirm("Do you want to input a new API key?")
        if retry:
            return configure_api_key()
        else:
            console.print("[magenta]Have a good day!")
            exit(1)


        


