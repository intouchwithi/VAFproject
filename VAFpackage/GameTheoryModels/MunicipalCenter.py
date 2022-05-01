__all__ = ('MunicipalCenter',)

class MunicipalCenter:
    def __init__(self, *, function, pmin = 0, pmax = None, step):
        self.p = pmin
        self.pBounds = [(pmin, pmax)]
        self.function = function
        self.benefit = 0
        self.step = step

    def calculate_benefit(self, *, S, p, lamb=None):
        if lamb is None:
            return self.function(S=S, p=p)
        else:
            return self.function(S=S, p=p, lamb=lamb)