from typing import Union, List, Dict, TypedDict
import os
from rich.console import Console

console = Console()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

class Fact(TypedDict):
    fact: str

class Quote(TypedDict):
    quote : str
    author : str
    category : str

class AnimalsInfo(TypedDict):
    name : str
    taxonomy : Dict[str, str]
    locations : List[str]
    characteristics : Dict[str, str]

categories   = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday", "business", "car", "change", "communication", "computers", "cool", "courage", "dad", "dating", "death", "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith", "family", "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future", "god", "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope", "humor", "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning", "legal", "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"]

categories_noun = {
    "alone": "loneliness",
    "amazing": "amazement",
    "best": "excellence",
    "cool": "coolness",
    "famous": "fame",
    "funny": "humor",
    "good": "goodness",
    "great": "greatness",
    "inspirational": "inspiration",
    "legal": "legality",
    "medical": "medicine",
}