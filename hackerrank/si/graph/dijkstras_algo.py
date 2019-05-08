#!/usr/bin/python3

# Dijkstra’s shortest path algorithm

from collections import defaultdict

INT_MAX = (1 << 32) - 1


class Graph:
    def __init__(self, N, M):
        self.G = defaultdict(list)
        self.V = N
        self.E = M

    def insert(self, u, v, w):
        self.G[u].append((v, w))
        self.G[v].append((u, w))

    def insertMin(self, arr, x):
        # if node is present in minheap, update distance
        status = False
        for i in arr:
            if x[1] == i[1]:
                i[0] = x[0]
                status = True
                break

        if not status:
            arr.append(x)
        N = len(arr)
        idx = N - 1

        while idx > 0 and arr[idx] < arr[(idx-1)//2]:
            arr[(idx-1)//2], arr[idx] = arr[idx], arr[(idx-1)//2]
            idx = (idx-1) // 2

    def delMin(self, arr):
        N = len(arr)
        if N == 1:
            return arr.pop(0)
        temp = arr[0]
        arr[0] = arr.pop()
        self.heapify(arr, 0, len(arr))
        return temp

    def heapify(self, arr, idx, N):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2

        if left < N and arr[left][0] < arr[smallest][0]:
            smallest = left
        if right < N and arr[right][0] < arr[smallest][0]:
            smallest = right

        if smallest != idx:
            arr[smallest], arr[idx] = arr[idx], arr[smallest]
            self.heapify(arr, smallest, N)

    def isInMinHeap(self, pq, v):
        for i in pq:
            if v == i[1]:
                return True
        return False

    def dijkstra(self, S):
        pq = []  # Min heap
        N = self.V
        dis = [INT_MAX] * (N+1)  # distance array
        self.insertMin(pq, [0, S])
        dis[S] = 0

        while pq:
            print("Min Heap: ", pq)
            d, u = self.delMin(pq)
            print("popped item: ", d, u)
            print("distance: ", dis)
            for i in self.G[u]:
                v = i[0]
                w = i[1]
                nd = d + w
                if dis[v] > nd:
                    dis[v] = nd
                    # update distance of node in minheap
                    self.insertMin(pq, [nd, v])
        print("distance: ", dis)


if __name__ == '__main__':
    N, M = map(int, input().split())
    obj = Graph(N, M)
    for _ in range(M):
        u, v, w = map(int, input().split())
        obj.insert(u, v, w)
    obj.dijkstra(3)
