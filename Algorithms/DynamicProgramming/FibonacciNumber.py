import math


# Most fastest way to calculate fibonaci number
def fibonacci(n):
    # Golden number
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))


if __name__ == '__main__':
    print(fibonacci(1000))
