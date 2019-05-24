#!/usr/bin/python3

# using Max Heap


def build_max_heap(arr, idx):
    p = (idx-1) // 2
    while p > 0 and arr[idx] > arr[p]:
        arr[idx], arr[p] = arr[p], arr[idx]
        idx = p


def getMax(arr):
    return arr[0]


def getSecondMax(arr, N):
    idx = 0
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < N:
        idx = left

    if right < N and arr[right] > arr[left]:
        idx = right
    return arr[idx]


def heapify(arr, idx, N):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < N and arr[largest] < arr[left]:
        largest = left
    if right < N and arr[largest] < arr[right]:
        largest = right

    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, N)


def optimal_ticket_seller(arr, N, K):
    # build max heap
    # print("arr: ", arr)
    tickets = 1
    revenue = 0
    for i in range(N-1, -1, -1):
        build_max_heap(arr, i)
    # print("arr: ", arr)

    # import pdb; pdb.set_trace()
    while tickets <= K:
        # print("arr: ", arr)
        # print("revenue: ", revenue)
        first_max = getMax(arr)
        if first_max == 0:
            break

        # second max element
        second_max = getSecondMax(arr, N)
        # print(first_max, second_max)

        while first_max >= second_max:
            if tickets > K or first_max == 0:
                break
            revenue += first_max
            first_max -= 1
            tickets += 1
        arr[0] = first_max
        heapify(arr, 0, N)
    return revenue


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(optimal_ticket_seller(arr, N, K))
