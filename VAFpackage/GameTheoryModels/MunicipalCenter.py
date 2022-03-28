__all__ = ('MunicipalCenter',)

class MunicipalCenter:
    def __init__(self, *, function, pmin = 0, pmax = None, eps = 0.01):
        self.p = pmin
        self.pBounds = [(pmin, pmax)]
        self.function = function
        self.benefit = 0
        self.eps = eps


    def calculate_benefit(self, *, S, p):
        return self.function(S=S, p=p)