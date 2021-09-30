import itertools


def by_first_element(t):
    return t[0]


def by_last_element(t):
    return t[-1]


A = [(1, 3, 5, 6, 6), (0, 1, 2, 4, 5), (1, 9, 8, 3, 5), (0, 2, 3, 5, 7)]
sorted_A = sorted(A, key=by_first_element)
groups = [[*g] for _, g in itertools.groupby(sorted_A, key=by_first_element)]
max_of_each_group = [max(g, key=by_last_element) for g in groups]
print(max_of_each_group)
