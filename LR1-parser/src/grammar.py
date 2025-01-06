from rule import Rule
import sys

class Grammar:
    rules = []
    nonterminals = set()
    terminals = set()

    def __init__(self, grammar_rules):
        for rule in grammar_rules:
            self.rules.append(Rule(rule[0], rule[1]))
            self.nonterminals.add(rule[0])
            for symbol in rule[1]:
                if not self.is_nonterminal(symbol):
                    self.terminals.add(symbol)

    def add_rule(self, rule):
        self.rules.append(Rule(rule[0], rule[1]))
        self.nonterminals.add(rule[0])
        for symbol in rule[1]:
            if not self.is_nonterminal(symbol):
                self.terminals.add(symbol)

    def __str__(self):
        return "\n".join(str(rule) for rule in self.rules)
    
    def is_nonterminal(self, symbol):
        return symbol.isalpha() and symbol.isupper()
    

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
