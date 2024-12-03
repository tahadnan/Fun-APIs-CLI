import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apis_handling import load_api_key, configure_api_key, fact, animal, quote, celebrity
from .constants import console, welcome_message, quote_topics, help_message
from prompt_toolkit import prompt, HTML

def prompt_animal(api_key : str) -> None:
    try:
        animal_name = prompt(HTML("<ansibrightblue>Which Animal are you looking for?</ansibrightblue> "))
        animal(api_key=api_key , animal_name=animal_name)
    except (EOFError,KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

def prompt_quote(api_key : str) -> None:
    try:
        console.print(quote_topics)
        quote_category = prompt(HTML("<ansimagenta>You want a quote about what ?[Leave blank for a random topic]</ansimagenta> "))
        quote(api_key=api_key,category=quote_category)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

def prompt_celebrity(api_key : str) -> None:
    try:
        celebrity_name = prompt(HTML("<ansimagenta>Who are you looking for ?</ansimagenta> "))
        celebrity(api_key=api_key, celeb_name=celebrity_name)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

def display_help_message() -> None:
    console.print(f"[green]{help_message}")

def exit_script() -> None:
    console.print("[bright_yellow]Have a good day!")
    exit(0)

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
    "celebrity" : prompt_celebrity
}

def invalid_option(option : str) -> None:
    console.print(f"[orange_red1]{option} is invalid, run 'help' to check the available commands.")

def launch_interactive(option : str) -> None:
    choice = options.get(option.strip().lower(), None)
    if not choice:
        invalid_option(option)
    elif option.lower().strip() in ["1", "help", "2", "configure", "exit", "3"]:
        choice()
    else:
        api_key = load_api_key()
        if choice is fact:
            choice(api_key)
        else:
            choice(api_key=api_key) 

def interactive_mode() -> None:
    try:
        console.print(f"[green bold]{welcome_message}[/green bold]")
        while True:
            option = prompt(HTML(f"<ansibrightcyan>Which one do you want: </ansibrightcyan>"))
            launch_interactive(option)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        exit_script()
