from grammar import Grammar

def get_first(grammar):
    first = {i: set() for i in grammar.nonterminals}
    first.update((i, {i}) for i in grammar.terminals)
    epsilon = set()
    
    while True:
        updated = False
        
        for rule in grammar.rules:
            for symbol in rule.right:
                updated |= union(first[rule.left], first[symbol])
                if symbol not in epsilon:
                    break
            else:
                updated |= union(epsilon, {rule.left})
                
        if not updated:
            return first


def union(first, begins):
    n = len(first)
    first |= begins
    return len(first) != n

