#!/usr/bin/python3


def range_subarray(arr, N, A, B):
    ans = 0
    for i in range(0, N+1):
        cur = 0
        for j in range(i+1, N+1):
            cur += arr[j]
            if cur in range(A, B+1):
                ans += 1
            print(arr[i:j])
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N, A, B = map(int, input().split())
        arr = list(map(int, input().split()))
        print(range_subarray(arr, N, A, B))
