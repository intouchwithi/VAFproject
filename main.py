from VAFpackage import TwoLevelModel, EconomicAgent, MunicipalCenter,ThreeLevelModel,FederalCenter
import math
import matplotlib.pyplot as plt
from functools import partial
import numpy as np


def analytical_Sf_function(S,*,Sf0,S0,degree,curve_down):
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

s = []
p = []
deg=[]
Sf=[]


S0=250
Sf0=100
a=4/S0
sigma=0.5
mu=1

a1=np.arange(-10,0,1)
a2=np.arange(2,10,1)
a3=np.concatenate((a1,a2))
b3=np.concatenate((np.ones(len(a1))*False,np.ones(len(a2))*True))

for degree, curve_down in zip(a3, b3):
    ecol_function = partial(analytical_Sf_function, S0=S0, Sf0=Sf0, degree=abs(degree), curve_down=curve_down)
    t = TwoLevelModel(S0=S0, a=a, ecol_function=ecol_function, step_ea=1e-6, step_mc=1e-6)
    t.find_equilibrium()
    deg.append(degree)
    s.append(t.economic_agent.S)
    p.append(t.municipal_center.p)
    Sf.append(ecol_function(S=t.economic_agent.S))
    if degree==-1:
        print(t.economic_agent.S, t.municipal_center.p,ecol_function(S=t.economic_agent.S))

#s = []
#p = []
#deg=[]
#Sf=[]


# for degree, curve_down in zip(a3, b3):
#     ecol_function = partial(analytical_Sf_function, S0=S0, Sf0=Sf0, degree=abs(degree), curve_down=curve_down)
#     t = ThreeLevelModel(S0=S0,a=a,sigma=sigma, mu=mu, ecol_function=ecol_function, step_ea=1e-6, step_fc=1e-6, step_mc=1e-3)
#     t.find_equilibrium()
#     deg.append(degree)
#     print(degree)
#     s.append(t.economic_agent.S)
#     p.append(t.municipal_center.p)
#     Sf.append(ecol_function(S=t.economic_agent.S))
#     if degree==-1:
#         print(t.economic_agent.S, t.municipal_center.p,ecol_function(S=t.economic_agent.S))

#plt.plot([i/S0 for i in s],[sf/Sf0 for sf in Sf])
plt.plot(deg,[i/S0 for i in s])
plt.show()
