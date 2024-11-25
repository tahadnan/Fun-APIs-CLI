import argparse
import requests
from rich.console import Console
from API_handling import fact, animal, quote, load_api_key
from Interactive_mode import interactive_mode

console = Console()

parser = argparse.ArgumentParser(
                    prog='Fun APIs',
                    description='Playing with some Ninjas APIs',
                    epilog='Enjoy it!')

parser.add_argument("-i","--interactive", help="Displays a random fact.", action='store_true')
parser.add_argument("-f","--fact", help="Displays a random fact.", action='store_true')
parser.add_argument("-a","--animal",metavar="animal_name", help="Displays animal(s) information.", nargs="+",type=str)
parser.add_argument("-q","--quote", metavar="quote_topic" ,help="Displays a random quote.", type=str)

args = parser.parse_args()

api_key = load_api_key()
if args.interactive:
    interactive_mode()
if args.fact:
    fact(api_key)  
if args.animal:
    animal(api_key," ".join(args.animal))  
if args.quote:
    quote(api_key,args.quote)  
