#!/usr/bin/python3

"""
Given an undirected graph represented as an adjacency matrix and an integer k,
determine whether each node in the graph can be colored such that no
two adjacent nodes share the same color using at most k colors.
"""


class Graph:
    def __init__(self, V):
        self.V = V
        self.G = [[0 for i in range(V)] for j in range(V)]
        self.colors = [-1] * (V)

    def colorable(self, K):
        if self.colorableUtil(0, K):
            return True
        return False

    def colorableUtil(self, S, K):
        print("colors: ", self.colors)
        if self.V == S:
            return True

        for i in range(0, K):
            if self.valid(S, i):
                self.colors[S] = i
                if self.colorableUtil(S+1, K):
                    return True
        return False

    def valid(self, u, k):
        for i in range(self.V):
            # find neighbour and if source color matches with
            # neighbour then return False
            if self.G[u][i] == 1 and self.colors[i] == k:
                return False
        return True


if __name__ == '__main__':
    g = Graph(4)
    g.G = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]
    K = 3
    print("Yes") if g.colorable(K) else print("No")
