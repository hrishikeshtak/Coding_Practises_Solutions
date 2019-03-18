#!/usr/bin/python3


def subsets_lexicographical_order(arr, N, idx, cur):
    if idx == N:
        return

    if cur:
        print(*cur)

    for i in range(idx+1, N):
        cur.append(arr[i])
        subsets_lexicographical_order(arr, N, i, cur)
        cur.pop()


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        subsets_lexicographical_order(arr, N, -1, [])
        print()
