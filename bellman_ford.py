from PriorityQueue import PriorityQueue
from utils         import *

name = 'bellman_ford'

def bellman_ford(pq, adjlist, weights):
    for _ in range(len(set(adjlist))-1):
        for u, v in [(u, v) for u in adjlist.keys() for v in adjlist[u]]:
            if pq.dist[v] > pq.dist[u] + weights[(u, v)]:
                pq.dist[v] = pq.dist[u] + weights[(u, v)]
                pq.prev[v] = u
                pq.decrease(v)

# Make an adjacency list and edge-weight dict for a given directed graph
adjlist = defaultdict(list)
weights = {}
elf = Array(Input(name))
n, e = elf[0]
for edge in elf[1:]:
    adjlist[edge[0]].append(edge[1])
    weights[(edge[0], edge[1])] = edge[2]

# Make an initial PriorityQueue from the original node distances of infinity
pq = PriorityQueue(n)
pq.make()

# Run Dijkstra's algorithm on the graph and printed values ordered by key
bellman_ford(pq, adjlist, weights)
dist = OrderedDict(sorted(pq.dist.items(), key=lambda t: t[0]))
print(rosalind_pretty(['x' if v == float('inf') else v for v in dist.values()]))
