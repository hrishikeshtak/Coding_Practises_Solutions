#!/usr/bin/python3


# Iterative
def check_subsequence(s1, s2):
    M = len(s1)
    N = len(s2)
    i = j = 0

    while i < M and j < N:
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == M:
        return "Yes"
    return "No"


# Recursive
def solve(s1, M, s2, N):
    if M == 0:
        return "Yes"
    if N == 0:
        return "No"

    if s1[M-1] == s2[N-1]:
        return solve(s1, M-1, s2, N-1)
    return solve(s1, M, s2, N-1)


def check_subsequence_recursive(s1, s2):
    M = len(s1)
    N = len(s2)
    return solve(s1, M, s2, N)


if __name__ == '__main__':
    for _ in range(int(input())):
        s1, s2 = input().split()
        print(check_subsequence(s1, s2))
        print(check_subsequence_recursive(s1, s2))
