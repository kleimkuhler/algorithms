from utils import *

name = 'topological'

def topological(above):
    "Topologically sort a DAG by removing a layer of sources until empty."
    result = []
    while above:
        sources = set(above) - set(flatten(above.values()))
        result.extend(sources)
        for node in sources:
            del above[node]
    return result

above = defaultdict(list)
for edge in Array(Input(name))[1:]:
    above[edge[0]].append(edge[1])
    above[edge[1]]
print(rosalind_pretty(topological(above)))
