from grammar import Grammar
from table import Table

class LR1Parser:
    grammar = Grammar
    parsing_table = {}
    final_reduce = str

    def __init__(self):
        pass

    def fit(self, grammar):
        self.final_reduce = f'{grammar.rules[-1].left}->{grammar.rules[-1].right[:-1]}'
        self.parsing_table = Table(grammar).build_parsing_table()

    def predict(self, input_string):
        stack = [0]
        input_string += '$'
        cursor = 0

        while True:
            state = stack[-1]
            lookahead = input_string[cursor]
            action = self.parsing_table.get(f'{state}+{lookahead}')

            if action is None:
                return False
            elif action.startswith('shift'):
                _, next_state = action.split()
                stack.append(lookahead)
                stack.append(int(next_state))
                cursor += 1
            elif action.startswith('reduce'):
                _, production = action.split(' ', 1)
                if production == self.final_reduce:
                    return True
                lhs, rhs = production.split('->')
                for _ in range(2 * len(rhs)):
                    stack.pop()
                goto_state = stack[-1]
                stack.append(lhs)
                stack.append(int(self.parsing_table[f'{goto_state}+{lhs}'].split()[1]))
            else:
                print("Error: Invalid syntax")
                return False

"""
grammar = Grammar ([['S', 'CC'],
                    ['C', 'cC'],
                    ['C', 'd']])
grammar.add_rule(['^', 'S$'])
# print(grammar)
# print(grammar.nonterminals, grammar.terminals)
parser = LR1Parser()
parser.fit(grammar)
# print(parser.parsing_table)
parser.predict('cdd')
"""