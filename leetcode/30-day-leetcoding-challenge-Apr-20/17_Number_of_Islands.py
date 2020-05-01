#!/usr/bin/python3


"""
Number of Islands
"""


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid:
            return 0

        cnt = 0
        R = len(grid)
        C = len(grid[0])

        for i in range(0, R):
            for j in range(0, C):
                if grid[i][j] == '1':
                    cnt += 1
                    self.DFS(grid, i, j, R, C)

        return cnt

    def valid(self, i, j, R, C):
        if i < 0 or j < 0 or i >= R or j >= C:
            return False
        return True

    def DFS(self, grid, i, j, R, C):
        # N-4 neighbourhood
        di = [0, 0, 1, -1]
        dj = [-1, 1, 0, 0]

        if self.valid(i, j, R, C):
            if grid[i][j] == '1':
                grid[i][j] = '0'

                for k in range(0, 4):
                    self.DFS(grid, i + di[k], j + dj[k], R, C)


if __name__ == '__main__':
    mat = [['1', '1', '1', '1', '0'],
           ['1', '1', '0', '1', '0'],
           ['1', '1', '0', '0', '0'],
           ['0', '0', '0', '1', '1']]

    print(f"{Solution().numIslands(mat)}")
    mat = [["1", "1", "0", "0", "0"],
           ["1", "1", "0", "0", "0"],
           ["0", "0", "1", "0", "0"],
           ["0", "0", "0", "1", "1"]]
    print(f"{Solution().numIslands(mat)}")
    mat = []
    print(f"{Solution().numIslands(mat)}")
