from rule import Rule

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