class Rule:
    left    = str
    right   = str

    def __init__(self, left_rule, right_rule):
        self.left   = left_rule
        self.right  = right_rule

    def __str__(self):
        return f"{self.left} -> {self.right}"