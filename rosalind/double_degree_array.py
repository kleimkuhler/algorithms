from itertools import chain

def double_degree_array(A, n):
    d = {vertex: [] for vertex in range(1, n+1)}

    for edge in A:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])

    degree_sums = []
    for vertex, neighbors in d.items():
        degree_sum = 0
        for neighbor in neighbors:
            degree_sum += len(d[neighbor])
        degree_sums.append(degree_sum)

    return degree_sums
            
with open('/home/kleimkuhler/Downloads/rosalind_ddeg.txt') as f:
    n, m = map(int, f.readline().strip().split())
    edges = [[int(i) for i in line.strip().split()] for line in f]

    print(' '.join(str(x) for x in double_degree_array(edges, n)))
