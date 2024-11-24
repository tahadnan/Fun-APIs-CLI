import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from API_handling.facts import fact
from .interactive_functions import prompt_animal, prompt_quote
from prompt_toolkit import prompt, HTML
from rich.console import Console

console = Console()

welcome_message = """
Hello and welcome to Fun APIs interactive mode. Here are the available options:
    1 - fact (Get you a fun fact)
    2 - animals (Let you fetch infos about a certain animal)
    3 - quote (Give you a quote about a certain topic)
P.S: You can use the numbers (e.g: 1 for fact) or the string itself (e.g: fact)
"""

options = {
    "1" : fact,
    "fact" : fact,
    "2" : prompt_animal,
    "animals" : prompt_animal,
    "3" : prompt_quote,
    "quote" : prompt_quote 
}

try:
    console.print(f"[green bold]{welcome_message}[/green bold]")
    option = prompt(HTML(f"<ansibrightcyan>Which one do you want: </ansibrightcyan>"))
    def invalid_option():
        console.print(f"[orange_red1]{option} is invalid.")
    def launch_interactive():
        options.get(option, invalid_option)()
except (EOFError, KeyboardInterrupt):
    print("Exiting...")
    sys.exit("Have a good day!")
