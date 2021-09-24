def factorial(n):
    if n == 0:
        return 1
    else:
        return float(n * factorial(n - 1))


print('Number of generations?')
K = float(input())
print('At least how many AaBb organisms?')
N = float(input())
a = 2 ** K  # found the error!!!
b = factorial(a)
c = factorial(a - N) * factorial(N)
d = (b // c) * (0.25 ** N) * (0.75 ** (a - N))
e = []
while N <= a:
    c = factorial(a - N) * factorial(N)
    val = (b // c) * (0.25 ** N) * (0.75 ** (a - N))
    e.append(val)
    N = N + 1
print('The probability of at least X organisms AaBb is:')
print(round(sum(e), 3))  # P(X ≥ x)