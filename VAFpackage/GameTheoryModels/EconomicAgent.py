__all__ = ('EconomicAgent',)

class EconomicAgent:
    def __init__(self, *, function, Smin = 0, Smax = None,eps):
        self.S = Smin
        self.SBounds = [(Smin, Smax)]
        self.function = function
        self.benefit = 0
        self.eps = eps

    def calculate_benefit(self, *, S, p):
        return self.function(S=S, p=p)