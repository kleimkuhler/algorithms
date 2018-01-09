from itertools import combinations
from numba import jit
from utils import *

name = 'sum3'

zero = lambda A: sum(A) == 0

def sum3(data):
    for line in data:
        trio = first_true(combinations(line, 3), zero)
        if trio:
            print(rosalind_pretty(Indices(line, trio)))
        else:
            print(-1)

data = Array(Input(name))
sum3(data[1:])
