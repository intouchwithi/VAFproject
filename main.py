from VAFpackage import TwoLevelModel, EconomicAgent, MunicipalCenter
import math
from functools import partial
import matplotlib as mpl
import matplotlib.pyplot as plt

def Sf_function(*,Sf0,S0,S):
    return -Sf0*S/S0+Sf0

def fagent(S,*,p,a,Sf0,S0,k):
    return a*S*math.pow(Sf_function(Sf0=Sf0, S0=S0, S=S),k)-S*p

def fmunicipal(p,*,S):
    return S*p


s = []
p = []

a=4/250
S0=250
Sf0=100
k=2
for i in range(-10,10,1):
    print(i)
    t=TwoLevelModel(economic_agent=EconomicAgent(function = fagent,Smin = 0, Smax = S0),
                    municipal_center=MunicipalCenter(function = fmunicipal,pmin = 0),
                    a=a,S0=S0,Sf0=Sf0,k=k)
    t.find_equilibrium()
    s.append(t.economic_agent.S)
    p.append(t.municipal_center.p)

plt.plot(range(-10,10,1),s)
plt.show()
