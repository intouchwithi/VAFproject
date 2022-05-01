from scipy.optimize import basinhopping,minimize,brute,fmin
from functools import partial
from . import EconomicAgent, MunicipalCenter, FederalCenter
import numpy as np

__all__ = ('ThreeLevelModel',)


class ThreeLevelModel:

    def _agent_function(self,S, *, p, a, ecol_function):
        return a * S * ecol_function(S) - S * p

    def _municipal_function(self,p, *, S, lamb, ecol_function):
        return S * p - lamb * (ecol_function(0) - ecol_function(S))

    def _federal_function(self,lamb, *, sigma, mu, S, ecol_function):
        return sigma * mu * ecol_function(S) + lamb * (ecol_function(0) - ecol_function(S))

    def __init__(self, *, S0, a, sigma, mu, ecol_function, step_ea, step_mc, step_fc):
        fagent = partial(self._agent_function, a=a, ecol_function=ecol_function)
        self.economic_agent = EconomicAgent(function=fagent, Smin=0, Smax=S0, step=step_ea)
        fmunicipal = partial(self._municipal_function, ecol_function=ecol_function)
        self.municipal_center = MunicipalCenter(function=fmunicipal, pmin=0, step=step_mc)
        ffederal = partial(self._federal_function, sigma=sigma, mu=mu, ecol_function=ecol_function)
        self.federal_center = FederalCenter(function=ffederal, lambmin=0, step=step_fc)

    def _maximize(self, function, bound, step):
        return minimize(lambda x: -function(x), [0], method = 'Nelder-Mead', bounds=bound, tol=step)

    def _find_best_S(self, current_p):
        rez = self._maximize(partial(self.economic_agent.function, p=current_p),
                             self.economic_agent.SBounds,
                             self.economic_agent.step)
        self.economic_agent.S = rez.x[0]

    def _find_best_p(self, current_lamb):

        def _current_municipal_benefit(current_p):
            self._find_best_S(current_p)
            return self.municipal_center.calculate_benefit(lamb=current_lamb,
                                                           p=current_p,
                                                           S=self.economic_agent.S)

        rez = self._maximize(_current_municipal_benefit,
                             self.municipal_center.pBounds,
                             self.municipal_center.step)
        self.municipal_center.p = rez.x[0]
        self.municipal_center.benefit = -rez.fun
        self.economic_agent.benefit = self.economic_agent.calculate_benefit(S=self.economic_agent.S,
                                                                            p=self.municipal_center.p)

    def _find_best_lamb(self):

        def _current_federal_benefit(current_lamb):
            self._find_best_p(current_lamb)
            return self.federal_center.calculate_benefit(lamb=current_lamb,
                                                         S=self.economic_agent.S)

        rez = self._maximize(_current_federal_benefit,
                             self.federal_center.lambBounds,
                             self.federal_center.step)
        self.federal_center.lamb = rez.x[0]
        self.federal_center.benefit = -rez.fun
        self.municipal_center.benefit = self.municipal_center.calculate_benefit(S=self.economic_agent.S,
                                                                                p=self.municipal_center.p,
                                                                                lamb=self.federal_center.lamb)

    def find_equilibrium(self):
        self._find_best_lamb()
