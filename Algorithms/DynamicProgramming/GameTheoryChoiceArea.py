# Python code to get maximum survival time

# Class to represent an area
class area:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def max_survival(A, B, X, Y, Z, last, memo):
    # if any of A or B is less than 0, return 0
    if A <= 0 or B <= 0:
        return 0
    cur = area(A, B)

    for ele in memo.keys():
        if cur.a == ele.a and cur.b == ele.b:
            return memo[ele]

    if last == 1:
        temp = 1 + max(max_survival(A + Y.a, B + Y.b,
                                    X, Y, Z, 2, memo),
                       max_survival(A + Z.a, B + Z.b,
                                    X, Y, Z, 3, memo))
    elif last == 2:
        temp = 1 + max(max_survival(A + X.a, B + X.b,
                                    X, Y, Z, 1, memo),
                       max_survival(A + Z.a, B + Z.b,
                                    X, Y, Z, 3, memo))
    elif last == 3:
        temp = 1 + max(max_survival(A + X.a, B + X.b,
                                    X, Y, Z, 1, memo),
                       max_survival(A + Y.a, B + Y.b,
                                    X, Y, Z, 2, memo))

    memo[cur] = temp

    return temp


def get_max_survival_time(A, B, X, Y, Z):
    if A <= 0 or B <= 0:
        return 0
    memo = dict()

    return max(max_survival(A + X.a, B + X.b, X, Y, Z, 1, memo),
               max_survival(A + Y.a, B + Y.b, X, Y, Z, 2, memo),
               max_survival(A + Z.a, B + Z.b, X, Y, Z, 3, memo))


X = area(3, 2)
Y = area(-5, -10)
Z = area(-20, 5)

A = 20
B = 8
print(get_max_survival_time(A, B, X, Y, Z))
