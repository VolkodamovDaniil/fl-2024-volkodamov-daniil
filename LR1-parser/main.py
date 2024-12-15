from grammar import Grammar
from lr1_parser import LR1Parser
import sys


def validate_input():
    try:
        nonterminals_number, terminals_number, rules_number = map(int, input().split())
        if not (0 <= nonterminals_number <= 100 and 0 <= terminals_number <= 100 and 0 <= rules_number <= 100):
            print("The numbers must be non-negative and not exceed 100")
            sys.exit(1) 
    except ValueError as e:
        print(f"First input line error: {e}")
        sys.exit(1)

    nonterminals = input().strip()
    if len(nonterminals) != nonterminals_number or not all(c.isupper() for c in nonterminals):
        print(f"The second line must contain exactly {nonterminals_number} of uppercase Latin letters.")
        sys.exit(1)

    terminals = input().strip()
    if len(terminals) != terminals_number or not all(c.islower() or c.isdigit() or c in "()+-*/[]{}" for c in terminals):
        print(f"The third line must contain exactly {terminals_number} alphabetic characters (lowercase Latin letters, digits, brackets, or arithmetic operation characters).")
        sys.exit(1)

    nonterminals = set(nonterminals)
    terminals = set(terminals)

    grammar = Grammar([])
    grammar.terminals = terminals
    grammar.nonterminals = nonterminals

    for _ in range(rules_number):
        rule = input().strip()
        left, right = rule.split('->')
        left = left.strip()
        right = right.strip()

        if left not in nonterminals:
            print(f"The nonterminal character '{left}' is not found in the list of nonterminal characters.")
            sys.exit(1)

        if right and any(symbol not in nonterminals | terminals for symbol in right):
            print(f"Error: The right side of the rule ‘{right}’ contains invalid characters.")
            sys.exit(1)
            
        grammar.add_rule([left, right])

    start_symbol = input().strip()
    if start_symbol not in nonterminals:
        print(f"Error: The start character '{start_symbol}' is not found in the list of non-terminal characters.")
        sys.exit(1)

    try:
        words_number = int(input().strip())
        if not (1 <= words_number <= 100000):
            print("The number of words must be between 1 and 100000.")
            sys.exit(1)
    except ValueError as e:
        print(f"Word number error: {e}")
        sys.exit(1)

    words = []
    for _ in range(words_number):
        word = input().strip()
        if any(symbol not in terminals for symbol in word):
            print(f"The word '{word}' contains invalid characters.")
            sys.exit(1)
        words.append(word)

    return start_symbol, grammar, words

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

"""
input:
2 2 3
SC
cd
S -> CC
C -> cC
C -> d
S
2
cdd
ccdd

output:
Yes
Yes
"""