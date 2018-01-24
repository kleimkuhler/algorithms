from PriorityQueue import PriorityQueue
from utils         import *

name = 'negative_weight'

def negative_weight(pq, adjlist, weights):
    for _ in range(len(adjlist.keys())-1):
        for u, v in [(u, v) for u in adjlist.keys() for v in adjlist[u]]:
            if pq.dist[v] > pq.dist[u] + weights[(u, v)]:
                pq.dist[v] = pq.dist[u] + weights[(u, v)]
                pq.prev[u] = u
                pq.decrease(v)
    for u, v in [(u, v) for u in adjlist.keys() for v in adjlist[u]]:
        if pq.dist[v] > pq.dist[u] + weights[(u, v)]:
            return True
    return False

# Make an adjacency list and edge-weight dict for given directed graphs
i, graphs, G = 1, 0, defaultdict(list)
lines = Array(Input(name))
while i != len(lines):
    n, e = lines[i]
    G[graphs].append(lines[i])
    for _ in range(e):
        i += 1
        G[graphs].append(lines[i])
    i += 1
    graphs += 1

results = []
for g in range(len(G.keys())):
    adjlist = defaultdict(list)
    weights = {}
    n, e = G[g][0]
    for edge in G[g][1:]:
        adjlist[edge[0]].append(edge[1])
        weights[(edge[0], edge[1])] = edge[2]
    pq = PriorityQueue(n)
    pq.make()
    results.append(1 if negative_weight(pq, adjlist, weights) else -1)
print(rosalind_pretty(results))
