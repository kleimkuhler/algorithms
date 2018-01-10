from utils import *

name = 'inversions'

def walk(A):
    inversions, seen = 0, []
    for val in A:
        inversions += len([x for x in seen if x > val])
        seen.append(val)
    return inversions

print(walk(Array(Input(name))[1]))
