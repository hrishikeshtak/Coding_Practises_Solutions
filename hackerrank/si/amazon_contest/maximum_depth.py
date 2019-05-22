#!/usr/bin/python3

from collections import defaultdict, deque


class Graph:
    def __init__(self, N):
        self.N = N
        self.G = defaultdict(list)
        self.depth = 0
        self.levels = defaultdict(list)

    def insert(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def maxDepth(self):
        # using BFS
        Q = deque()
        visited = [False] * (self.N+1)
        # add node and its level in Q
        Q.append((1, 0))
        Q.append((None, 0))
        visited[1] = True

        while len(Q) > 1:
            u, level = Q.popleft()
            if u:
                self.levels[level].append(u)

                for i in self.G[u]:
                    if visited[i] is False:
                        visited[i] = True
                        Q.append((i, level+1))
            else:
                self.depth += 1
                Q.append((None, 0))

        # print("maxDepth: %s" % (self.depth))
        # print("levels: ", self.levels)

    def query(self, A, L, X):
        L = L % (self.depth + 1)
        for i in self.levels[L]:
            if A[i-1] >= X:
                return A[i-1]
        return -1


if __name__ == '__main__':
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    g = Graph(N)
    for _ in range(0, N-1):
        u, v = map(int, input().split())
        g.insert(u, v)
    # find max depth of Tree
    g.maxDepth()
    # Query
    for _ in range(Q):
        L, X = map(int, input().split())
        print(g.query(arr, L, X))
