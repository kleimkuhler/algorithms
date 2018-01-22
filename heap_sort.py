from utils import *

from build_heap import heapify, build_heap

name = 'heap_sort'

def heap_sort(A):
    """Heap sort A by building a max heap and repeating n-1 times:
    1. Swap the last element of the heap with its root
    2. Heapify the new root on a heap size n-1"""
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return A

print(rosalind_pretty(heap_sort(list(Array(Input(name))[1]))))
