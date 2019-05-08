#!/usr/bin/python3

# Is Forest
# Forest contains >=1 Trees (#CC >= 1)
# Trees:
#   # CC = 1
#   acyclic


from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)

    def insert(self, u, v):
        # undirected
        self.G[u].append(v)
        self.G[v].append(u)

    def isForest(self, N):
        visited = [False] * (N+1)
        visited[0] = True
        status = True
        for i in range(1, N+1):
            # print("visited: ", visited)
            if visited[i] is False:
                # check each CC is Tree or not (acyclic)
                status = self.isTree(i, visited)
                if status is False:
                    break
        return status

    def isTree(self, i, visited):
        if (self.isCyclic(i, -1, visited)):
            # print("Graph is Cyclic")
            # Graph is cyclic, not Tree
            return False
        # print("Graph is Acyclic")
        return True

    def isCyclic(self, u, parent, visited):
        visited[u] = True

        for i in self.G[u]:
            # if node is not visited, then again traverse thr its
            # neighbours and mark True
            if visited[i] is False:
                if self.isCyclic(i, u, visited):
                    return True
            # if visited node is not parent then cycle exist
            elif i != parent:
                return True
        return False


if __name__ == '__main__':
    for _ in range(int(input())):
        obj = Graph()
        N, M = map(int, input().split())
        for _ in range(0, M):
            u, v = map(int, input().split())
            obj.insert(u, v)
        status = obj.isForest(N)
        if status:
            print("Yes")
        else:
            print("No")
