''' Python program to find size of array after repeated
deletion of LIS '''

# Function to construct Maximum Sum LIS
from typing import List


def findLIS(arr: List[int], n: int) -> List[int]:
    L = [0] * n
    for i in range(n):
        L[i] = []

    L[0].append(arr[0])
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                    (len(L[i]) < len(L[j]))):
                L[i] = L[j].copy()
        L[i].append(arr[i])
    maxSize = 1
    lis: List[int] = []
    for x in L:
        if (len(x) > maxSize):
            lis = x.copy()
            maxSize = len(x)

    return lis

def minimize(input: List[int], n: int) -> None:
    arr = input.copy()
    while len(arr):
        lis = findLIS(arr, len(arr))
        if (len(lis) < 2):
            break
        i = 0
        while i < len(arr) and len(lis) > 0:
            if (arr[i] == lis[0]):
                arr.remove(arr[i])
                i -= 1
                lis.remove(lis[0])
            i += 1
    i = 0
    while i < len(arr):
        print(arr[i], end=" ")
        i += 1
    if (i == 0):
        print("-1")

if __name__ == "__main__":
    input = [3, 2, 6, 4, 5, 1]
    n = len(input)
    minimize(input, n)
