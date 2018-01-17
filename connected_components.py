def explore(graph, start, visited):
    for neighbor in graph.get(start):
        if neighbor not in visited:
            visited.add(neighbor)
            explore(graph, neighbor, visited)

def dfs(graph):
    visited = set()
    scc = 0
    for node in graph:
        if node not in visited:
            explore(graph, node, visited)
            scc += 1

    return scc

def connected_components(n, edges):
    # undirected adjacency list
    graph = {node: set() for node in range(1, n+1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    return dfs(graph)

with open('/Users/oog250/Downloads/rosalind_cc.txt') as f:
    n, m = map(int, f.readline().strip().split())
    edges = [[int(i) for i in line.strip().split()] for line in f]
    print(connected_components(n, edges))
