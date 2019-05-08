#!/usr/bin/python3
# BFS with distance array |V|*(|V| + |E|)

from collections import defaultdict


class Graph:
    def __init__(self, N, M):
        self.G = defaultdict(list)
        self.V = N
        self.E = M

    def insert(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def length_of_the_longest_path(self):
        ans = 0
        for i in self.G:
            ans = max(ans, self.BFS(i))
        return ans

    def BFS(self, s):
        Q = []
        d = [-1] * (self.V+1)
        d[s] = 0
        Q.append(s)

        while Q:
            u = Q.pop(0)
            for i in self.G[u]:
                if d[i] == -1:
                    d[i] = d[u] + 1
                    Q.append(i)
        return max(d)


if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().split())
        obj = Graph(N, M)
        for _ in range(M):
            u, v = map(int, input().split())
            obj.insert(u, v)
        print(obj.length_of_the_longest_path())
