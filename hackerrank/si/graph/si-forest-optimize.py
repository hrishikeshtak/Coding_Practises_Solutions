#!/usr/bin/python3

# Is Forest
# Forest contains >=1 Trees (#CC >= 1)
# Trees:
#   # CC = 1
#   acyclic


from collections import defaultdict


class Graph:
    def __init__(self, N, M):
        self.G = defaultdict(list)
        self.E = M
        self.V = N

    def insert(self, u, v):
        # undirected
        self.G[u].append(v)
        self.G[v].append(u)

    def isForest(self):
        visited = [False] * (self.V + 1)
        visited[0] = True
        cc = 0
        for i in range(1, self.V + 1):
            # print("visited: ", visited)
            if visited[i] is False:
                cc += 1
                # check each CC is Tree or not (acyclic)
                self.DFS(i, visited)
        # print("Connected Components: %s" % (cc))
        # Acycle = |E| == |V| - CC
        return self.E == self.V - cc

    def DFS(self, u, visited):
        visited[u] = True

        for i in self.G[u]:
            # if node is not visited, then again traverse thr its
            # neighbours and mark True
            if visited[i] is False:
                self.DFS(i, visited)


if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().split())
        obj = Graph(N, M)
        for _ in range(0, M):
            u, v = map(int, input().split())
            obj.insert(u, v)
        status = obj.isForest()
        if status:
            print("Yes")
        else:
            print("No")
