from collections import Counter
from itertools import chain

def degree_array(edge_list):
    endpoints = [edge for edge in chain.from_iterable(edge_list)]
    degrees = Counter(endpoints)
    return [degrees[key] for key in sorted(degrees, key = int)]

# with open('rosalind_deg.txt') as f:
with open('/home/kleimkuhler/Downloads/rosalind_deg.txt') as f:
    next(f) # skip first line
    edge_list=[line.split() for line in f]

    print(' '.join(str(x) for x in degree_array(edge_list)))
