#!/usr/bin/python3

# using DFS
# Given an undirected graph, you have to find if there exists a
# path between 2 given nodes of the graph.


from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)

    def insert(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def DFS(self, s, d, visited):
        # print("Graph: ", self.G)
        # print(s, d)
        if visited[s]:
            return False
        visited[s] = True
        if s == d:
            return True

        for i in self.G[s]:
            if self.DFS(i, d, visited):
                return True

        return False


if __name__ == '__main__':
    for i in range(int(input())):
        obj = Graph()
        N, M = map(int, input().split())
        for _ in range(0, M):
            u, v = map(int, input().split())
            obj.insert(u, v)
        Q = int(input())
        print("Test Case #%s:" % (i+1))
        for _ in range(0, Q):
            visited = [False] * (N+1)
            s, d = map(int, input().split())
            status = obj.DFS(s, d, visited)
            if status:
                print("Yes")
            else:
                print("No")
