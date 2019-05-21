#!/usr/bin/python3

# Using BFS 2-colorable(0, 1)


class Graph:
    def __init__(self, V):
        self.V = V
        self.G = [[0 for i in range(V)] for j in range(V)]

    def bipartite(self, S):
        # initialize with 2
        colors = [2] * (self.V)
        Q = []

        # assign color 1 to source node
        colors[S] = 1
        Q.append(S)

        while Q:
            print("colors: ", colors)
            print("Q: ", Q)
            u = Q.pop()

            # self loop, not possible to color using 2-colors
            if self.G[u][u] == 1:
                return False

            for v in range(self.V):
                if self.G[u][v] == 1 and colors[v] == 2:
                    colors[v] = 1 - colors[u]
                    Q.append(v)
                elif self.G[u][v] == 1 and colors[u] == colors[v]:
                    return False
        return True


if __name__ == '__main__':
    g = Graph(4)
    g.G = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]
    print("Yes") if g.bipartite(0) else print("No")
