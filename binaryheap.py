from utils import *

name = 'binaryheap'

def heapify(A, i):
    "Heapify A by sifting down A[i] into its children."
    start = i
    left = 2 * start + 1
    right = 2 * start + 2
    if left < len(A) and A[start] < A[left]:
        start = left
    if right < len(A) and A[start] < A[right]:
        start = right
    if start != i:
        A[i], A[start] = A[start], A[i]
        heapify(A, start)

def heap_sort(A):
    "Heap sort an array in decreasing order."
    for i in range(len(A)-1, -1, -1):
        heapify(A, i)
    return A

print(rosalind_pretty(heap_sort(list(Array(Input(name))[1]))))
