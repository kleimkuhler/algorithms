def partition(A):
    pivot = 0
    left, right = 1, len(A)-1
    
    while left+1 != right:
        while A[left] <= A[pivot]:
            left += 1
        while A[right] > A[pivot]:
            right -= 1
        A[left], A[right] = A[right], A[left]
        
    A[pivot], A[left] = A[left], A[pivot]
    return A
        

with open("/home/kleimkuhler/Downloads/rosalind_par.txt") as f:
    n = int(f.readline().strip())
    A = list(map(int, f.readline().strip().split()))
    print(' '.join(map(str, partition(A))))
