from rich.console import Console

console = Console()

available_topics = ['age', 'loneliness', 'amazement', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'excellence', 'birthday', 'business', 'car', 'change', 'communication', 'computers', 'coolness', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'fame', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'humor', 'future', 'god', 'goodness', 'government', 'graduation', 'greatness', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspiration', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legality', 'life', 'love', 'marriage', 'medicine', 'men', 'mom', 'money', 'morning', 'movies', 'success']

quote_topics = f'''
[yellow i]Available topics are:[/yellow i]
[bright_cyan bold]\t{"\n\t".join([category.capitalize() for category in available_topics])}[/bright_cyan bold]
'''

welcome_message = """
Hello and welcome to Fun APIs interactive mode. Here are the available options:
    1 - help (Displays a help message)
    2 - configure (Let you configure and set up your ninjas' API key)
    3 - exit (Exits the script)
    4 - fact (Get you a fun fact)
    5 - animals (Let you fetch infos about a certain animal)
    6 - quote (Give you a quote about a certain topic)
P.S: You can use the numbers (e.g: 1 for help) or the string itself (e.g: help)
"""
help_message = '''
Here are the available options:
    1 - help (Displays a help message)
    2 - configure (Let you configure and set up your ninjas' API key)
    3 - exit (Exits the script)
    4 - fact (Get you a fun fact)
    5 - animals (Let you fetch infos about a certain animal)
    6 - quote (Give you a quote about a certain topic)
P.S: You can use the numbers (e.g: 1 for help) or the string itself (e.g: help)
'''
