import os
from collections import defaultdict

t9 = {
    "1": ".,?!'\"-_@$%&",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
slownik_words = defaultdict(list)

BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, "slownik_plik.txt")
#tworzy sciezke do pliku

with open(PATH, encoding="utf-8") as f:  #with gwarantuje zamknięcie pliku aytomatyczne
    for w in f:
        w = w.strip()
        if w:
            slownik_words[len(w)].append(w)

