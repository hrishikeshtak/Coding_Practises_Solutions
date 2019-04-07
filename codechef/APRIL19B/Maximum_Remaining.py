#!/usr/bin/python3


def max_remaining(arr, N):
    arr.sort()
    i = N - 1
    j = N - 2
    ans = -(1 << 31)

    while i >= 0:
        res = max((arr[i] % arr[j]), (arr[j] % arr[i]))
        # print(res, arr[i], arr[j])
        ans = max(ans, res)
        i -= 1
    return ans


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_remaining(arr, N))
