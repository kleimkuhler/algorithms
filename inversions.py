from utils import *

name = 'inversions'

def walk(A):
    inversions = 0
    for i, val in enumerate(A):
        inversions += len([x for x in A[0:i] if x > val])
    return inversions

print(walk(Array(Input(name))[1]))
