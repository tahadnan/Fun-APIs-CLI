import argparse
from .apis_handling import fact, animal, quote, celebrity, superhero
from .configuration import load_api_key, configure_api_key
from .interactive_cli import interactive_mode
from .helper_functions import display_superheroes_table

def main_entry():
    parser = argparse.ArgumentParser(
                        prog='fun_apis.py',
                        description='Playing with some APIs',
                        epilog='Enjoy it!',
                        allow_abbrev=False)

    parser.add_argument("-c","--config", help="Launch API configuring process.", action='store_true')
    parser.add_argument("-i","--interactive", help="Displays a random fact.", action='store_true')
    parser.add_argument("-f","--fact", help="Displays a random fact.", action='store_true')
    parser.add_argument("-a","--animal",metavar="animal_name", help="Displays animal(s) information.", nargs="+",type=str)
    parser.add_argument("-q","--quote", help="Displays a random quote.", action='store_true')
    parser.add_argument("-sc","--search-celebrity",metavar="celebrity_name", help="Displays a celebrity information.", nargs="+",type=str)
    parser.add_argument("-ss","--search-superhero",metavar="sup_name", help="Displays a superhero information.", nargs="+",type=str)
    parser.add_argument("-st","--superhero-table", help="Displays superheroes table.", action='store_true')

    args = parser.parse_args()

    if args.config:
        configure_api_key() 
    elif args.interactive:
        interactive_mode()
    elif args.fact:
        fact(api_key=load_api_key(which_api_key="ninjas_api_key"))  
    elif args.animal:
        animal(api_key=load_api_key(which_api_key="ninjas_api_key"),animal_name=" ".join(args.animal))
    elif args.quote:
        quote(api_key=load_api_key(which_api_key="ninjas_api_key"))
    elif args.search_celebrity :
        celebrity(api_key=load_api_key(which_api_key="ninjas_api_key"),celeb_name=" ".join(args.search_celebrity))
    elif args.search_superhero :
        superhero(api_key=load_api_key(which_api_key="superhero_api_key"),superhero_id_or_name=" ".join(args.search_superhero))
    elif args.superhero_table:
        display_superheroes_table()
        
if __name__ == "__main__":
    main_entry()