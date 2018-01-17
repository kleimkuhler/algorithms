from utils import *

name = 'bfs'

def adjacency_table(lines):
    adjtable = defaultdict(list)
    for line in lines:
            adjtable[line[0]].append(line[1])
    return adjtable

def step_table(adjtable):
    keys, seen = [1], []
    stable = {key: -1 for key in range(1, max(adjtable.keys())+1)}
    for step in count(0):
        for key in keys:
            stable[key] = step
            seen.append(key)
        keys = [v for key in keys for v in adjtable[key] if v not in seen]
        if not keys:
            return stable
    
adjtable = adjacency_table(Array(Input(name))[1:])
stable = step_table(adjtable)
ostable = OrderedDict(sorted(stable.items(), key=lambda t: t[0]))
print(rosalind_pretty([v for k, v in ostable.items()]))
