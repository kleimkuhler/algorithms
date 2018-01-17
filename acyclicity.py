from utils import *

name = 'acyclicity'

def adjacency_list(elf):
    "Create an adjacency list from edge-list format."
    adjlist = defaultdict(list)
    for edge in elf[1:]:
        adjlist[edge[0]].append(edge[1])
    return adjlist

def cyclic(root, adjlist, visited):
    "Determine if a path of nodes through an adjacency list is cyclical."
    visited.add(root)
    for neighbor in adjlist[root]:
        if neighbor in visited or cyclic(neighbor, adjlist, visited):
            return True
    visited.remove(root)
    return False

def dfs(adjlist):
    "Depth first search through an adjacency list for any cyclical paths."
    return any(cyclic(node, adjlist, set()) for node in set(adjlist))

i, graphs = 0, defaultdict(list)
lines = Input(name)
for line in lines:
    if not line.strip():
        i += 1
        continue
    graphs[i].append(Vector(line))

results = []
for g in range(1, i+1):
    adjlist = adjacency_list(graphs[g])
    results.append(-1 if dfs(adjlist) else 1)
print(rosalind_pretty(results))
