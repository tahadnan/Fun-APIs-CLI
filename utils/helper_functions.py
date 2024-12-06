from functools import wraps
import os
import json
from json import JSONDecodeError
from typing import Callable, Union
from requests import ConnectionError
from constants import console, SUPERHEROES_JSON_FILE_PATH

def error_handler(func : Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError:
            console.print("[red]No internet connection! Please check your network and try again.[/red]")
            return None
        except Exception as error:
            console.print(f"[red]An error has occured:[/red]\n{error}")
            return None
    return wrapper

def meters_to_freedom_units(meters : Union[int, float]) -> str:
    total_feet = meters * 3.28084  
    feet = int(total_feet)         
    inches = (total_feet - feet) * 12  
    return f"{feet}'{round(inches)}\""

def verify_superhero (superhero_id_or_name : Union[int, str]):
    try:
        with open(SUPERHEROES_JSON_FILE_PATH, "r") as ref_file:
            ref = json.load(ref_file)

        if isinstance(superhero_id_or_name,int) and superhero_id_or_name in ref.values():
            return True, superhero_id_or_name
        elif isinstance(superhero_id_or_name, str) and superhero_id_or_name.title() in ref.keys():
            return True, ref.get(superhero_id_or_name.title())
        else:
            return False, None
    except JSONDecodeError as err:
        console.print(f"[red]Broken or invalid JSON file:\"{SUPERHEROES_JSON_FILE_PATH}\"\n{err}")
        return False, None

def cli_errors(func : Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except (EOFError, KeyboardInterrupt):
            print("Exiting...")
            sys.exit("Have a good day!")
    return wrapper


