from utils import *

class PriorityQueue:
    "A Priority Queue in a binary heap"

    dist = {}
    prev = {}
    Q = []

    def __init__(self, n):
        "Initialize node dists and prevs to infinity and None respectively."
        for node in range(1, n+1):
            self.dist[node] = inf
            self.prev[node] = None
        self.dist[1] = 0

    def _min(self, u, v):
        "Is the dist of u smaller than the dist of v."
        return self.dist[self.Q[u]] < self.dist[self.Q[v]]

    def _sift(self, i):
        "Recursively sift a node down the queue."
        start = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.Q) and self._min(left, start):
            start = left
        if right < len(self.Q) and self._min(right, start):
            start = right
        if start != i:
            self.Q[i], self.Q[start] = self.Q[start], self.Q[i]
            self._sift(start)

    def _bubble(self, i):
        "Recursively bubble a node up the queue."
        parent = (i - 1) // 2
        if i != 0 and self._min(i, parent):
            self.Q[i], self.Q[parent] = self.Q[parent], self.Q[i]
            self._bubble(parent)

    def make(self):
        "Make a Priority Queue from the set of nodes."
        self.Q.extend(set(self.dist))
        for i in range(len(self.Q)-1, -1, -1):
            self._sift(i)

    def decrease(self, node):
        "Decrease a node in the queue by bubbling up it's new dist value."
        self._bubble(self.Q.index(node))

    def delete(self):
        "Delete the min node. Set the last node as the first and sift it down."
        u = self.Q.pop(0)
        try:
            self.Q.insert(0, self.Q.pop(-1))
            self._sift(0)
        except IndexError:
            pass
        return u
