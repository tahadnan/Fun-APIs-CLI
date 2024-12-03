from functools import wraps
from typing import Callable, Union
from requests import ConnectionError
from json.decoder import JSONDecodeError
from prompt_toolkit.shortcuts import confirm
from .constants import console

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

