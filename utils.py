import math
import re

from collections import (defaultdict, OrderedDict)
from itertools import (chain, count)

flatten = chain.from_iterable

inf = float('inf')

def Input(name):
    filename = '{}.txt'.format(name)
    return open(filename)

def Array(lines):
    if isinstance(lines, str): lines = lines.splitlines()
    return mapt(Vector, lines)

def Vector(line):
    return mapt(Atom, line.replace(',', '').split())

def Indices(A, indices):
    return rosalind_index(mapt(A.index, indices))

def Atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

def mapt(fn, *args):
    return tuple(map(fn, *args))

def first_true(iterable, pred=None, default=None):
    return next(filter(pred, iterable), default)

def rosalind_index(A):
    "Rosalind and their indexing by 1..."
    return mapt(lambda x: x+1, A)

def rosalind_pretty(s):
    s = str(s)
    rep = {',': '', '(': '', ')': '', '[': '', ']': '', '\'': ''}
    for i, j in rep.items():
        s = s.replace(i, j)
    return s
