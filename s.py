
from random import seed
from random import randint
import numpy as np

def f5(n,A):
    sum=0
    min, max = 1,1
    for i in range(0,n):
        int_random =randint(0,1)
        if int_random == 0 :   # B is true
            if A[i] > A[max]:
                sum+=1
                max = i
            elif A[i] < A[min]:
                min = i
                sum+=1
    return sum


A = np.random.permutation(50)
print(A)
print(f5(A.size,A))