__all__ = ('FederalCenter',)

class FederalCenter:
    def __init__(self, *, function, lambmin = 0, lambmax = None, step):
        self.lamb = lambmin
        self.lambBounds = [(lambmin, lambmax)]
        self.function = function
        self.benefit = 0
        self.step = step


    def calculate_benefit(self, *, S, lamb):
        return self.function(S=S, lamb=lamb)