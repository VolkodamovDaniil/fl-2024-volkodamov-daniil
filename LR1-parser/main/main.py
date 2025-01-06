import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from grammar import Grammar, validate_input
from lr1_parser import LR1Parser


start_symbol, grammar, words = validate_input()
grammar.add_rule(['^', f'{start_symbol}$'])

parser = LR1Parser()
parser.fit(grammar)

# print(parser.parsing_table)

for word in words:
    if (parser.predict(word)):
        print("Yes")
    else:
        print("No")

