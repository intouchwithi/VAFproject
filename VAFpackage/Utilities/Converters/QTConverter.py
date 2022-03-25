import numpy as np
from ..MainConstants import Q_MAX, Q_MIN, T_MAX, T_MIN

__all__ = ('QTConverter',)


class QTConverter:
    def __init__(self):
        pass

    def convert(self, *, q, t):
        current_q = int(np.round(q/1000, 0))
        current_t = int(np.round(t, 0))

        if current_q > Q_MAX:
            print(f"There is no map with Q = {current_q} and t = {current_t} in the library")

            current_t = int(np.round((current_q * current_t) / Q_MAX, 0))
            current_q = Q_MAX

            if current_t > T_MAX:
                current_t = T_MAX
                print(f"Parameters were changed to maximum Q = {current_q} and t = {current_t}")
            else:
                print(f"Parameters were changed to Q = {current_q} and t = {current_t}")

        elif current_q < Q_MIN:
            print(f"There is no map with Q = {current_q} and t = {current_t} in the library")
            if current_q <= 0:
                current_q = Q_MIN
                current_t = T_MIN
                print(f"Parameters were changed to minimum Q = {current_q} and minimum t = {current_t}")
            else:
                current_q = Q_MIN
                current_t = int(np.round((current_q * current_t) / Q_MIN, 0))
                if current_t > T_MAX:
                    current_t = T_MAX
                    print(f"Parameters were changed to minimum Q = {current_q} and maximum t = {current_t}")
                else:
                    print(f"Parameters were changed to Q = {current_q} and t = {current_t}")

        else:
            if current_t > T_MAX:
                print(f"There is no map with Q = {current_q} and t = {current_t} in the library")
                current_q = int(np.round((current_q * current_t) / T_MAX, 0))
                current_t = T_MAX
                print(f"Parameters were changed to Q = {current_q} and t = {current_t}")

        return current_q, current_t
