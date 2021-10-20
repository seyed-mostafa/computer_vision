from random import seed
from random import randint
import numpy as np


def f5(n, A):
    sum = 0
    min, max = 1, 1
    for i in range(0, n):
        int_random = randint(0, 1)
        if int_random == 0:  # B is true
            if A[i] < A[min]:
                max = i
            elif A[i] > A[max]:
                min = i
                sum += 1
            elif A[i] < A[min]:
                sum += 1
                max = i
    return sum


# sum=0
# A = np.random.permutation(50)
# print(++sum)
# print(sum)
import math

while (True):
    n = int(input("n = "))
    results = 0
    for t in range(0, math.floor(math.log(math.floor(n / 2), 5)) + 1):
        i = math.floor(n / 5 ** t)
        print(i)
        results += (math.floor(math.log(i, 5)) + 1) * i

    print(results)
