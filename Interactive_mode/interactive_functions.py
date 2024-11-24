import sys
from API_handling import animal, quote
from prompt_toolkit import prompt, HTML
from rich.console import Console

console = Console()

def prompt_animal():
    try:
        animal_name = prompt(HTML("<ansibrightblue>Which Animal are you looking for?</ansibrightblue> "))
        animal(animal_name)
    except (EOFError,KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

available_topics = ['age', 'loneliness', 'amazement', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'excellence', 'birthday', 'business', 'car', 'change', 'communication', 'computers', 'coolness', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'fame', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'humor', 'future', 'god', 'goodness', 'government', 'graduation', 'greatness', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspiration', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legality', 'life', 'love', 'marriage', 'medicine', 'men', 'mom', 'money', 'morning', 'movies', 'success']

quote_topics = f'''
[yellow i]Available topics are:[/yellow i]
[bright_cyan bold]\t{"\n\t".join([category.capitalize() for category in available_topics])}[/bright_cyan bold]
'''
def prompt_quote():
    try:
        console.print(quote_topics)
        quote_category = prompt(HTML("<ansimagenta>You want a quote about what ?[Leave blank for a random topic]</ansimagenta> "))
        quote(quote_category)
    except (EOFError, KeyboardInterrupt):
        print("Exiting...")
        sys.exit("Have a good day!")

