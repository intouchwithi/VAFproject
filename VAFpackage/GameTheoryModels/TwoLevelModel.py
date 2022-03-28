from scipy.optimize import basinhopping,minimize,brute,fmin
from functools import partial
import numpy as np

__all__ = ('TwoLevelModel',)


class TwoLevelModel:
    def __init__(self, *, economic_agent, municipal_center):
        self.economic_agent = economic_agent
        self.municipal_center = municipal_center

    def _maximize(self, function, bound, eps):
        return minimize(lambda x: -function(x), [0], bounds=bound, tol=eps)
        #return brute(lambda x: -function(x), (slice(bound[0][0],bound[0][1],eps)), full_output=True, finish=fmin)

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
        self.municipal_center.benefit = -rez.fun
        self.economic_agent.benefit = self.economic_agent.calculate_benefit(S=self.economic_agent.S,
                                                                            p=self.municipal_center.p)

    def find_equilibrium(self):
        self._find_best_p()
