from PriorityQueue import PriorityQueue
from utils         import *

name = 'cte'

def cte(pq, adjlist, weights, start):
    "Dijkstra's algorithm to find the shortest cycle from start node."
    import pdb; pdb.set_trace()
    while pq.Q:
        u = pq.delete()
        for v in adjlist[u]:
            if pq.dist[v] > pq.dist[u] + weights[(u, v)]:
                pq.dist[v] = pq.dist[u] + weights[(u, v)]
                pq.prev[v] = u
                pq.decrease(v)
            if v == start:
                return pq.dist[u] + weights[(u, v)]
    return -1

# Read input into a dictionary of graphs
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

# For each graph, find if there is a cycle through the first edge
results = []
for g in range(len(G.keys())):
    adjlist, weights = defaultdict(list), {}
    n, e = G[g][0]
    start, node, weight = G[g][1]
    for edge in G[g][1:]:
        adjlist[edge[0]].append(edge[1])
        weights[(edge[0], edge[1])] = edge[2]
    adjlist[start] = [node]
    pq = PriorityQueue(n, start)
    pq.make()
    results.append(cte(pq, adjlist, weights, start))
print(rosalind_pretty([-1 if v == float('inf') else v for v in results]))
