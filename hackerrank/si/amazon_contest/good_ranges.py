#!/usr/bin/python3

# Brute Force


def query(Q, N):
    Q.sort()
    # print(Q)
    M = len(Q)
    if M == 1:
        return 1 + N

    ans = 0
    for i in range(0, M):
        # first element
        if i == 0:
            ans += 1
        elif i == M-1:
            ans += N

        # lower range
        if i > 0:
            ans += Q[i-1] + 1
        # upper range
        if i < M-1:
            ans += Q[i+1] - 1

    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    Q = []
    A = set()
    for _ in range(M):
        X = int(input())
        if X not in A:
            A.add(X)
            Q.append(X)
            ans = query(Q, N)
            print(ans)
        else:
            print(ans)
