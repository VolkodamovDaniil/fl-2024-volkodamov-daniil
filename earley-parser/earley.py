from grammar import Grammar
from situation import Situation


class Earley:
    grammar = Grammar 
    D_situations = {} 
    start = str

    def __init__(self, start_symbol):
        self.start = start_symbol

    def add_situation(self, situation, D_idx):
        for state in self.D_situations[D_idx]:
            if (state == situation):
                return
        
        self.D_situations[D_idx].add(situation)

    def predict(self, D_idx):
        new_situations = []
        for state in self.D_situations[D_idx]:
            if state.point_idx < len(state.beta):
                unterminal = state.beta[state.point_idx] 
                for rule in self.grammar.rules:
                    if rule.left == unterminal:
                        new_state = Situation(unterminal, rule.right, D_idx, 0)
                        new_situations.append(new_state)

        for state in new_situations:
            self.add_situation(state, D_idx)

    def scan(self, D_idx, terminal):
        for state in self.D_situations[D_idx]:
            if state.point_idx < len(state.beta) and state.beta[state.point_idx] == terminal:
                new_state = Situation(state.alpha, state.beta, state.word_idx, state.point_idx + 1)
                self.add_situation(new_state, D_idx + 1)

    def complete(self, D_idx):
        new_situations = []
        for state in self.D_situations[D_idx]:
            D_internal_idx = state.word_idx
            if state.point_idx == len(state.beta):
                for state_internal in self.D_situations[D_internal_idx]:
                    if state_internal.point_idx < len(state_internal.beta) and state_internal.beta[state_internal.point_idx] == state.alpha:
                        new_state = Situation(state_internal.alpha, state_internal.beta, state_internal.word_idx, state_internal.point_idx + 1)
                        new_situations.append(new_state)
        
        for state in new_situations:
            self.add_situation(state, D_idx)

    def fit(self, earley_grammar):
        self.grammar = earley_grammar
        self.grammar.add_rule(('S#', 'S'))

    def is_recognised(self, word):
        self.D_situations = {}
        state = Situation('S#', self.start, 0, 0)
        self.D_situations[0] = set()
        self.D_situations[0].add(state)
        for i in range(1, len(word) + 1):
            self.D_situations[i] = set()

        while True:
            prev_len = len(self.D_situations[0])
            self.predict(0)
            self.complete(0)
            new_len = len(self.D_situations[0])
            if prev_len == new_len:
                break

        for i in range(1, len(word) + 1):
            self.scan(i - 1, word[i - 1])
            while True:
                prev_len = len(self.D_situations[i])
                self.predict(i)
                self.complete(i)
                new_len = len(self.D_situations[i])
                if prev_len == new_len:
                    break

        desired_situation = Situation('S#', 'S', 0, 1)

        if desired_situation in self.D_situations[len(word)]:
            return True

        return False
    
