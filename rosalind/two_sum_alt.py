def two_sum_alt(A):
    for i in range(len(A)):
        try:
            match = A.index(-A[i], i+1)
            return [i+1, match+1]
        except ValueError:
            pass

    return [-1]

with open('/home/kleimkuhler/Downloads/rosalind_2sum.txt') as f:
    k, n = f.readline().strip().split()
    data = [[int(i) for i in line.strip().split()] for line in f.readlines()]

    for d in data:
        print(' '.join(map(str, two_sum_alt(d))))
