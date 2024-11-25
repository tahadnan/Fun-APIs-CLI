import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from API_handling import fact,animal, quote, load_api_key
from .constants import console, welcome_message, quote_topics
from prompt_toolkit import prompt, HTML

def prompt_animal(api_key : str):
    try:
        animal_name = prompt(HTML("<ansibrightblue>Which Animal are you looking for?</ansibrightblue> "))
        animal(api_key=api_key , animal_name=animal_name)
    except (EOFError,KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

def prompt_quote(api_key : str):
    try:
        console.print(quote_topics)
        quote_category = prompt(HTML("<ansimagenta>You want a quote about what ?[Leave blank for a random topic]</ansimagenta> "))
        quote(api_key=api_key,category=quote_category)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

options = {
    "1" : fact,
    "fact" : fact,
    "2" : prompt_animal,
    "animals" : prompt_animal,
    "3" : prompt_quote,
    "quote" : prompt_quote 
}

def invalid_option(option : str):
    console.print(f"[orange_red1]{option} is invalid.")

def launch_interactive(option : str):
    choice = options.get(option.strip(), None)
    if not choice:
        invalid_option(option)
        return 
    else:
        api_key = load_api_key()
        if choice is fact:
            print(choice)
            choice(api_key)
        else:
            choice(api_key=api_key) 

def interactive_mode():
    try:
        console.print(f"[green bold]{welcome_message}[/green bold]")
        option = prompt(HTML(f"<ansibrightcyan>Which one do you want: </ansibrightcyan>"))
        launch_interactive(option)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")
