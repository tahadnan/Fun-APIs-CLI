from functools import wraps
from typing import Callable
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
        except JSONDecodeError:
            console.print("[red]Broken JSON file")
            retry = confirm("Do you want to input a new API key?")
            if retry:
                return configure_api_key()
            else:
                console.print("[magenta]Have a good day!")
                exit(1)
        except Exception as error:
            console.print(f"[red]An error has occurred:\n{error}")
            return None
    return wrapper
