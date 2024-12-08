from rule import Rule

class Grammar:
    rules = []

    def __init__(self, grammar_rules):
        for rule in grammar_rules:
            self.rules.append(Rule(rule[0], rule[1]))

    def add_rule(self, rule):
        self.rules.append(Rule(rule[0], rule[1]))

    def __str__(self):
        return "\n".join(str(rule) for rule in self.rules)