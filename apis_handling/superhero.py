from typing import Union
import json
import requests
from .constants import console
from .utils import error_handler, verify_superhero

@error_handler
def fetch_hero_info(api_key : str , superhero_id_or_name : Union[int, str]) :
    is_valid_arg, super_hero_id = verify_superhero(superhero_id_or_name)
    if is_valid_arg:
        api_url = f"https://superheroapi.com/api/{api_key}/{super_hero_id}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            console.print(f"[red]Failed to fetch superhero info. HTTP Status: {response.status_code}")
    else:
        console.print(f"[yellow]Invalid superhero identifier: {superhero_id_or_name}")
