from ..Utilities.MainConstants import THRESHOLD1, EPS
__all__ = ('f1', 'f2', 'f3', 'f4')


def f1(freq):
    if freq < THRESHOLD1*(1-EPS):
        return 0
    elif freq < THRESHOLD1:
        return (freq-1+EPS)/EPS
    else:
        return freq


def f2(freq):
    return (freq+1)/2


def f3(freq):
    if freq <= 0.5*EPS:
        return 1-2*freq/EPS
    else:
        return 0


def f4(freq):
    return 1-0.25*freq