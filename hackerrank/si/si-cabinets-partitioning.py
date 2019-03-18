#!/usr/bin/python3


def valid(arr, N, K, mid):
    min_time = arr[0]
    workers = 1
    for i in range(1, N):
        if min_time + arr[i] <= mid:
            min_time += arr[i]
        else:
            workers += 1
            # print("min_time: %s, workers: %s" % (min_time, workers))
            min_time = arr[i]

    if workers <= K:
        return True
    else:
        return False


def cabinets_partitioning(arr, N, K):
    lo = max(arr)
    hi = sum(arr)
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if valid(arr, N, K, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(cabinets_partitioning(arr, N, K))
