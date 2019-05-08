#!/usr/bin/python3

# Connected components using DFS
# connected components not reachable from node
# if not reachable from node: visited False, then increase count

from collections import defaultdict


class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self.G = defaultdict(list)

    def insert(self, u, v):
        # undirected graph
        self.G[u].append(v)
        self.G[v].append(u)

    def connected_components(self, N):
        # print("Graph: ", self.G)
        cnt = 0
        visited = [False] * (N+1)
        # 0 node is not needed

        for u in range(1, N+1):
            if visited[u] is False:
                cnt += 1
                self.DFS(u, visited)
        return cnt

    def DFS(self, s, visited):
        # print("s: %s visited: %s" % (s, visited))
        if visited[s]:
            return False

        visited[s] = True
        for i in self.G[s]:
            self.DFS(i, visited)


if __name__ == '__main__':
    for _ in range(int(input())):
        obj = Graph()
        N, M = map(int, input().split())
        for _ in range(0, M):
            u, v = map(int, input().split())
            obj.insert(u, v)
        print(obj.connected_components(N))
