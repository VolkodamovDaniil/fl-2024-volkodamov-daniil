import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from earley import Earley
from grammar import Grammar, validate_input


start_symbol, grammar, words = validate_input()

easrey_parser = Earley(start_symbol)
easrey_parser.fit(grammar)

for word in words:
    if easrey_parser.is_recognised(word):
        print("Yes")
    else:
        print("No")
