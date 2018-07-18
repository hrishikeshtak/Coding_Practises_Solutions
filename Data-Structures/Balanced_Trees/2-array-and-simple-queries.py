#!/usr/bin/python3

""" simple pythonic way, but Failed for testcase from 14 to 26,
due to Terminated due to timeout"""


# N, M = map(int, input().rstrip().split())

# seq = input().split()[:N]

# for _ in range(M):
#     _type, i, j = map(int, (input().split()))
#     if _type == 1:
#         seq = seq[(i-1):j] + seq[:(i-1)] + seq[j:]
#     elif _type == 2:
#         seq = seq[:(i-1)] + seq[j:] + seq[(i-1):j]

# # absolute difference
# print(abs(int(seq[0]) - int(seq[-1])))
# # print seq in one line
# print(*seq)
