import sys
import os
from apis_handling import load_api_key, configure_api_key, fact, animal, quote, celebrity, superhero
from constants import welcome_message, quote_topics, help_message, console
from utils import cli_errors
from prompt_toolkit import prompt, HTML

def display_help_message() -> None:
    console.print(f"[green]{help_message}")

def exit_script() -> None:
    console.print("[bright_yellow]Have a good day!")
    exit()

def invalid_option(option : str) -> None:
    console.print(f"[orange_red1]{option} is invalid, run 'help' to check the available commands.")

@cli_errors
def prompt_animal(api_key : str) -> None:
    animal_name = prompt(HTML("<ansibrightblue>Which Animal are you looking for?</ansibrightblue> "))
    animal(api_key=api_key , animal_name=animal_name)

@cli_errors
def prompt_quote(api_key : str) -> None:
    console.print(quote_topics)
    quote_category = prompt(HTML("<ansimagenta>You want a quote about what ?[Leave blank for a random topic]</ansimagenta> "))
    quote(api_key=api_key,category=quote_category)

@cli_errors
def prompt_celebrity(api_key : str) -> None:
    celebrity_name = prompt(HTML("<ansimagenta>Who are you looking for ?</ansimagenta> "))
    celebrity(api_key=api_key, celeb_name=celebrity_name)

@cli_errors
def prompt_superhero(api_key : str) -> None:
    sup_name = prompt(HTML("<ansimagenta>Which sup are you looking for ?</ansimagenta> "))
    superhero(api_key, sup_name)

def prompt_configure_api_key():
    pass

options = {
    "1" : display_help_message,
    "help" : display_help_message,
    "2" : configure_api_key,
    "configure" : configure_api_key,
    "3" : exit_script,
    "exit" : exit_script,
    "4" : fact,
    "fact" : fact,
    "5" : prompt_animal,
    "animal" : prompt_animal,
    "6" : prompt_quote,
    "quote" : prompt_quote,
    "7" : prompt_celebrity,
    "celebrity" : prompt_celebrity,
    "8" : prompt_superhero,
    "superhero" : prompt_superhero
}

def launch_interactive(option : str) -> None:
    choice = options.get(option.strip().lower(), None)
    if not choice:
        invalid_option(option)
    elif option.lower().strip() in ["1", "help", "2", "configure", "exit", "3"]:
        choice()
    else:
        if option.lower().strip() in ["4", "fact", "5", "animal", "6", "quote","7","celebrity"]:
            api_key = load_api_key(which_api_key="ninjas_api_key")
            if choice is fact:
                choice(api_key)
            else:
                choice(api_key=api_key) 
        elif option.lower().strip() in ["8","superhero"]:
            api_key = load_api_key(which_api_key="superhero_api_key")
            choice(api_key)

@cli_errors
def interactive_mode() -> None:
    console.print(f"[green bold]{welcome_message}[/green bold]")
    while True:
        option = prompt(HTML(f"<ansibrightcyan>Which one do you want: </ansibrightcyan>"))
        launch_interactive(option)
