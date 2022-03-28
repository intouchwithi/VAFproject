from VAFpackage import TwoLevelModel, EconomicAgent, MunicipalCenter
import math
import matplotlib.pyplot as plt
from functools import partial
import numpy as np


def analytical_Sf_function(*,Sf0,S0,S,degree,curve_down):
    if degree == 0:
        return Sf0
    elif degree == 1:
        return -Sf0*S/S0+Sf0
    else:
        if curve_down:
            temp = math.pow(S/S0,degree)
            return -Sf0 * temp + Sf0
        else:
            temp = math.pow((S0 - S) / S0, degree)
            return Sf0 * temp


def Sf_function(*,Sf0,S0,S):
    return -Sf0*S/S0+Sf0

def fagent(S,*,p,a,Sf0,S0,degree,curve_down):
    return a*S*analytical_Sf_function(Sf0=Sf0, S0=S0, S=S, degree=degree, curve_down=curve_down)-S*p

def fmunicipal(p,*,S):
    return S*p

s = []
p = []
deg=[]
Sf=[]

a=4/250
S0=250
Sf0=100


curve_down = False
for degree in np.arange(10,0,-1):
    ea = EconomicAgent(function = fagent,Smin = 0, Smax = S0)
    ea.function = partial(ea.function, a=a, S0=S0, Sf0=Sf0, degree=degree, curve_down=curve_down)
    mc = MunicipalCenter(function=fmunicipal, pmin=0)
    t = TwoLevelModel(economic_agent=ea, municipal_center=mc)
    t.find_equilibrium()
    deg.append(-degree)
    s.append(t.economic_agent.S)
    p.append(t.municipal_center.p)
    Sf.append(analytical_Sf_function(S=t.economic_agent.S, S0=S0, Sf0=Sf0, degree=degree, curve_down=curve_down))

curve_down = True
for degree in np.arange(2,10,1):
    ea = EconomicAgent(function=fagent, Smin=0, Smax=S0)
    ea.function = partial(ea.function, a=a, S0=S0, Sf0=Sf0, degree=degree, curve_down=curve_down)
    mc = MunicipalCenter(function=fmunicipal, pmin=0)
    t = TwoLevelModel(economic_agent=ea, municipal_center=mc)
    t.find_equilibrium()
    deg.append(degree)
    s.append(t.economic_agent.S)
    p.append(t.municipal_center.p)
    Sf.append(analytical_Sf_function(S=t.economic_agent.S, S0=S0, Sf0=Sf0, degree=degree, curve_down=curve_down))

plt.plot([i/S0 for i in s],[sf/Sf0 for sf in Sf])
plt.show()
