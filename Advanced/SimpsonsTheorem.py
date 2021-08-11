import numpy as np


def simpsonsTheorem(fn, a, b, n):
    x = np.linspace(a, b, n + 1)
    w = 2 * np.ones(n + 1)
    w[0] = 1.0
    w[-1] = 1
    for i in range(len(w)):
        if i % 2 == 1:
            w[i] = 4
    width = x[1] - x[0]
    area = 0.333 * width * np.sum(w * fn(x))
    return area


def f(x):
    return np.exp(x)


a = 0.1
b = np.pi

approxIntegral = simpsonsTheorem(f, a, b, 10000)
print(approxIntegral)
