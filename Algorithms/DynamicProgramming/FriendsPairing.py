import cmath
from collections import Callable


def laguerre_method(f_0: Callable, f_1: Callable, f_2: Callable, x0: float, n: float, epsilon: float = 0.00001):
    xk = x0
    while abs(f_0(xk)) > epsilon:
        G = f_1(xk) / f_0(xk)
        H = G ** 2 - f_2(xk) / f_0(xk)
        root = cmath.sqrt((n - 1) * (n * H - G ** 2))
        d = max(abs(G + root), abs(G - root))
        a = n / d
        xk -= a
    return xk

print(laguerre_method(f_0, f_1, f_2, 6, 3))