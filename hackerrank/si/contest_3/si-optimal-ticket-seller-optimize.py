#!/usr/bin/python3

from collections import defaultdict


# using dict, prefix sum
def optimal_ticket_seller(arr, N, K):
    # max ticket from all window
    m = max(arr)
    revenue = 0
    hashmap = defaultdict(lambda: 0)

    # initialize hashmap with tickets counter
    for i in range(N):
        hashmap[arr[i]] += 1
    # print("hashmap: ", hashmap)

    for i in range(0, K):
        if hashmap[m] > 1:
            revenue += m
            hashmap[m] -= 1
            hashmap[m-1] += 1
        elif hashmap[m] != 0:
            revenue += m
            # decrease ticket counter with 1
            m -= 1
            hashmap[m] += 1
    return revenue


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(optimal_ticket_seller(arr, N, K))
