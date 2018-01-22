from utils import *

name = 'build_heap'

def heapify(A, n, i):
    "Recursively sift down i if A[i] is smaller than either of it's children."
    largest = i
    left = 2 * largest + 1
    right = 2 * largest + 2
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def build_heap(A):
    "Build a max heap by heapifying n/2 elements in reverse."
    n = len(A)
    for i in range(n//2, -1, -1):
        heapify(A, n, i)
    return A

if __name__ == '__main__':
    print(rosalind_pretty(build_heap(list(Array(Input(name))[1]))))
