from itertools import combinations
from utils import *

name = 'sum3'

zero = lambda A: sum(A) == 0

def sum3(A):
    A.sort()
    for i in range(0, len(A)-2):
        j, k = i+1, len(A)-1
        while (j < k):
            if zero((A[i], A[j], A[k])):
                return (A[i], A[j], A[k])
            elif sum((A[i], A[j], A[k])) < 0:
                j += 1
            else:
                k -= 1
    return None

for line in Array(Input(name))[1:]:
    result = sum3(list(line))
    if result:
        result = list(Indices(line, result))
        print(rosalind_pretty(sorted(result)))
    else:
        print(-1)
