#!/usr/bin/python3

# using min heap


def heapify(arr, i, N):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < N and arr[left] < arr[smallest]:
        smallest = left

    if right < N and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest, N)


def insertMin(arr, x):
    arr.append(x)
    idx = len(arr) - 1

    while idx > 0 and arr[idx] < arr[(idx-1)//2]:
        arr[idx], arr[(idx-1)//2] = arr[(idx-1)//2], arr[idx]
        idx = (idx-1) // 2


def delMin(arr):
    N = len(arr)
    # If only one element in heap, do not heapify
    if N == 1:
        return arr.pop()

    # If 2 elements in heap
    temp = arr[0]
    arr[0] = arr.pop()
    N = len(arr)
    if N <= 1:
        return temp

    heapify(arr, 0, len(arr))
    return temp


def min_cost_to_connect_rods(arr, N):
    # build min heap
    # print("before heapify: ", arr)
    for i in range((N-1)//2, -1, -1):
        heapify(arr, i, N)
    # print("after heapify: ", arr)

    ans = 0
    while len(arr) != 1:
        # print("MinHeap: ", arr)
        a = delMin(arr)
        b = delMin(arr)

        # insert into min heap
        insertMin(arr, (a+b))
        ans += (a+b)
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(min_cost_to_connect_rods(arr, N))
