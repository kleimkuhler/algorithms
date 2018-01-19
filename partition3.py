from utils import *

name = 'partition3'

def partition3(A):
    pivot, pos = A[0], 1
    for step in count(0):
        if A[pos] > pivot:
            temp = A.pop(pos)
            A.insert(len(A), temp)
        elif A[pos] < pivot:
            temp = A.pop(pos)
            A.insert(0, temp)
            pos += 1
        else:
            pos += 1
        if step == len(A):
            return A

print(rosalind_pretty(partition3(list(Array(Input(name))[1]))))
