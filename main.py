import argparse
import sys
import requests
from requests import ConnectionError
from rich.console import Console
from API_handling import fact, animal, quote

console = Console()

parser = argparse.ArgumentParser(
                    prog='Fun APIs',
                    description='Playing with some Ninjas APIs',
                    epilog='Enjoy it!')

parser.add_argument("--fact", help="Displays a random fact.", action='store_true')
parser.add_argument("--animal", help="Displays animal information.", nargs="+",type=str)
parser.add_argument("--quote", help="Displays a random quote.", type=str)

args = parser.parse_args()


if args.fact:
    fact()  

if args.animal:
    animal(" ".join(args.animal))  

if args.quote:
    quote(args.quote)  

args = parser.parse_args()