__all__ = ('customMinimize',)


def parabolaApproximation(x1, x2, x3, y1, y2, y3):
    if abs(x1-x2) < 1e-8:
        return x2, y2
    else:
        temp1 = (y1 - y2) / (x1 - x2)
        temp2 = (y2 - y3) / (x2 - x3)
        a = (temp1 - temp2) / (x1 - x3)
        b = temp1 - a * (x1 + x2)
        c = y1 - a * x1 * x1 - b * x1
        if abs(a) < 1e-8:
            return x2, y2
        else:
            x_rez = -0.5 * b / a
            return x_rez,  a * x_rez * x_rez + b * x_rez + c


def customMinimize(*, function, bound, step):
        x1 = bound[0][0]
        x2 = bound[0][0]
        x3 = x1 + step
        y1 = function(x1)
        y2 = function(x1)
        y3 = function(x1 + step)

        while y2 >= y3:
            if bound[0][1] is not None:
                if x3 > bound[0][1]:
                    x3 = bound[0][1]
                    y3 = function(x3)
                    break
            x1 = x2
            y1 = y2
            x2 = x3
            y2 = y3
            x3 += step
            y3 = function(x3)

        x_min, y_min = parabolaApproximation(x1, x2, x3, y1, y2, y3)

        if bound[0][1] is not None:
            if x_min > bound[0][1]:
                x_min = bound[0][1]
                y_min = function(x_min)
        return CustomMinimum([x_min], y_min)


class CustomMinimum:
    def __init__(self, x_min, y_min):
        self.x = x_min
        self.fun = y_min
