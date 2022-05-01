__all__ = ('EconomicAgent',)

class EconomicAgent:
    def __init__(self, *, function, Smin = 0, Smax = None,step):
        self.S = Smin
        self.SBounds = [(Smin, Smax)]
        self.function = function
        self.benefit = 0
        self.step = step

    def calculate_benefit(self, *, S, p):
        return self.function(S=S, p=p)