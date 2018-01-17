from utils import *

name = 'bipartiteness'

def adjacency_list(elf):
    "Create an adjacency list from edge-list format."
    adjlist = defaultdict(list)
    for edge in elf[1:]:
        adjlist[edge[0]].append(edge[1])
        adjlist[edge[1]].append(edge[0])
    return adjlist

def bipartite(root, adjlist, colored, color, prev=None):
    "Check if root can be added to color without violating bipartiteness."
    if root in flatten(colored.values()):
        return True
    if any(neighbor in colored[color] for neighbor in adjlist[root]):
        return False
    colored[color].append(root)
    for neighbor in adjlist[root]:
        if neighbor == prev:
            continue
        if not bipartite(neighbor, adjlist, colored, 1-color, root):
            return False
    return True

def dfs(adjlist):
    "Depth first search through an adjacency list for bipartiteness."
    colored = defaultdict(list)
    return all(bipartite(node, adjlist, colored, 0) for node in set(adjlist))

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
    results.append(1 if dfs(adjlist) else -1)
print(rosalind_pretty(results))
