#!/usr/bin/python3

# using inbuilt min heap
import heapq


def min_cost_to_connect_rods(arr, N):
    # build min heap
    heapq.heapify(arr)

    ans = 0
    while len(arr) != 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        # insert into min heap
        heapq.heappush(arr, (a+b))
        ans += (a+b)
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(min_cost_to_connect_rods(arr, N))
