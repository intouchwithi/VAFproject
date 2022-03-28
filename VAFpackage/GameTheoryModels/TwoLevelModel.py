from scipy.optimize import basinhopping,minimize
from functools import partial
import numpy as np

__all__ = ('TwoLevelModel',)


class TwoLevelModel:
    def __init__(self, *, economic_agent, municipal_center, a, S0, Sf0,k):
        self.economic_agent = economic_agent
        self.economic_agent.function = partial(self.economic_agent.function, a=a, S0=S0, Sf0=Sf0, k=k)
        self.municipal_center = municipal_center

    def _maximize(self, function, bound, eps):
        return minimize(lambda x: -function(x), [0], bounds=bound, tol=eps)

    def _find_best_S(self, current_p):
        rez = self._maximize(partial(self.economic_agent.function, p=current_p),
                             self.economic_agent.SBounds,
                             self.economic_agent.eps)
        self.economic_agent.S = rez.x[0]

    def _find_best_p(self):

        def _current_municipal_benefit(current_p):
            self._find_best_S(current_p)
            return self.municipal_center.calculate_benefit(p=current_p,
                                                           S=self.economic_agent.S)

        rez = self._maximize(_current_municipal_benefit,
                             self.municipal_center.pBounds,
                             self.municipal_center.eps)
        self.municipal_center.p = rez.x[0]
        self.municipal_center.benefit = -rez.fun[0]
        self.economic_agent.benefit = self.economic_agent.calculate_benefit(S=self.economic_agent.S,
                                                                            p=self.municipal_center.p)

    def find_equilibrium(self):
        self._find_best_p()
