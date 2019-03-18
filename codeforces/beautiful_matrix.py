#!/usr/bin/python3

matrix = []
n = 5
center_pos = 2
count = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    if 1 in matrix[i]:
        # row movement
        count += abs(center_pos - i)
        for index, j in enumerate(matrix[i]):
            if j == 1:
                count += abs(center_pos - index)
print(count)
