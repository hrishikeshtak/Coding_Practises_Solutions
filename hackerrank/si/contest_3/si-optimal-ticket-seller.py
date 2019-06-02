#!/usr/bin/python3

# using Max Heap
import heapq


def getMax(arr):
    return heapq._heappop_max(arr)


def getSecondMax(arr):
    if arr:
        return arr[0]
    return 0


def optimal_ticket_seller(arr, N, K):
    # build max heap
    # print("arr: ", arr)
    revenue = 0
    heapq._heapify_max(arr)
    # print("arr: ", arr)

    while K > 0:
        # print("arr: ", arr)
        # print("revenue: ", revenue)
        first_max = getMax(arr)
        if first_max == 0:
            break

        # second max element
        second_max = getSecondMax(arr)
        # print("first_max: {}, second_max: {}".format(first_max, second_max))

        while first_max >= second_max:
            if K == 0:
                break
            revenue += first_max
            first_max -= 1
            K -= 1
        arr.append(first_max)
        heapq._heapify_max(arr)
    return revenue


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(optimal_ticket_seller(arr, N, K))
