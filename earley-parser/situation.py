class Situation:
    alpha       = str
    beta        = str
    word_idx    = int 
    point_idx   = int 

    def __init__(self, situation_alpha, situation_beta, situation_word_idx, situation_point_idx):
        self.alpha      = situation_alpha
        self.beta       = situation_beta
        self.word_idx   = situation_word_idx
        self.point_idx  = situation_point_idx

    def __eq__(self, other):
        if isinstance(other, Situation):
            return (self.alpha == other.alpha and
                    self.beta == other.beta and
                    self.word_idx == other.word_idx and
                    self.point_idx == other.point_idx)
        return False
    
    def __hash__(self):
        return hash((self.alpha, self.beta, self.word_idx, self.point_idx))