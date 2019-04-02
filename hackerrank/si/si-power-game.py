#!/usr/bin/python3


def power_game(A, B, N):
    A.sort()
    B.sort()
    p1 = 0
    p2 = 0
    cnt = 0
    # print(A)
    # print(B)
    while p1 < N and p2 < N:
        if A[p1] > B[p2]:
            p1 += 1
            p2 += 1
            cnt += 1
        else:
            p1 += 1
    return cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(power_game(A, B, N))
