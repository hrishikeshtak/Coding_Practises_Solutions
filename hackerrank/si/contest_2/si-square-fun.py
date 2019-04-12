#!/usr/bin/python3

import math


# def square_fun(A, B):
#     n = math.floor(math.sqrt(A))
#     m = math.floor(math.sqrt(B))
#     # print(n, m)
#     cnt = 0
#     for i in range(n, m+1):
#         # print(i)
#         if i*i in range(A, B+1):
#             cnt += 1
#     return cnt


def square_fun(A, B):
    n = math.ceil(math.sqrt(A))
    m = math.floor(math.sqrt(B))

    return m - n + 1


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = map(int, input().split())
        print(square_fun(A, B))
