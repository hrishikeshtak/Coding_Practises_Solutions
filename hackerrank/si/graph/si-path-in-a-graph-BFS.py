#!/usr/bin/python3

# using BFS
# Given an undirected graph, you have to find if there exists a
# path between 2 given nodes of the graph.


from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)

    def insert(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def BFS(self, s, d, N):
        # print("Graph: ", self.G)
        visited = [False] * (N+1)
        Q = []
        if s == d:
            return True
        Q.append(s)
        visited[s] = True

        while Q:
            u = Q.pop()
            for i in self.G[u]:
                if visited[i] is False:
                    visited[i] = True
                    if d == i:
                        return True
                    Q.append(i)
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
            s, d = map(int, input().split())
            status = obj.BFS(s, d, N)
            if status:
                print("Yes")
            else:
                print("No")
