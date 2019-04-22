#!/usr/bin/python3

from sys import stdin, stdout


def size(arr):
    return len(arr) - 1


def insert(arr, key):
    arr.append(key)

    # after addition, check heap property
    idx = size(arr)

    while idx > 1 and arr[idx] < arr[idx//2]:
        arr[idx], arr[idx//2] = arr[idx//2], arr[idx]
        idx = idx // 2


def getMin(arr):
    N = size(arr)
    if N == 0:
        # print("Empty")
        stdout.write(str("Empty") + "\n")
    else:
        # print(arr[1])
        stdout.write(str(arr[1]) + "\n")


def LeftChildren(arr, i):
    left = 2 * i
    if left >= size(arr):
        return -1

    return left


def RightChildren(arr, i):
    right = 2 * i + 1
    if right >= size(arr):
        return -1

    return right


def delMin(arr):
    # print("before delMin: ")
    # print(arr)

    # copy last element to 1st element and then maintain heap property
    N = size(arr)
    if N == 0:
        return
    elif N == 1:
        _ = arr.pop()
        return

    arr[1] = arr.pop()
    heapify_iterative(arr, 1)
    # heapify_recursive(arr, 1)
    # print("After delMin: ")
    # print(arr)


def heapify_iterative(arr, idx):
    left = LeftChildren(arr, idx)
    right = RightChildren(arr, idx)

    while left != -1 or right != -1:
        # find smallest index value from l and r
        smallest = idx
        if left != -1 and arr[left] < arr[smallest]:
            smallest = left
        if right != -1 and arr[right] < arr[smallest]:
            smallest = right

        if smallest != idx:
            arr[idx], arr[smallest] = arr[smallest], arr[idx]
            break
        idx = smallest
        left = LeftChildren(arr, idx)
        right = RightChildren(arr, idx)


def heapify_recursive(arr, idx):
    smallest = idx
    left = LeftChildren(arr, idx)
    right = RightChildren(arr, idx)

    # find min index from l and r
    if left != -1 and arr[left] < arr[smallest]:
        smallest = left
    if right != -1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        heapify_recursive(arr, smallest)


def implementHeap(arr, op):
    if op[0].lower() == "insert":
        x = int(op[1].rstrip())
        # x = int(op[1])
        insert(arr, x)

    elif op[0].rstrip().lower() == "getmin":
        getMin(arr)

    elif op[0].rstrip().lower() == "delmin":
        delMin(arr)
    else:
        print("Invalid Operation")
        return


if __name__ == '__main__':
    arr = [None]
    for _ in range(int(input())):
        op = stdin.readline().split(" ", 1)
        # op = input().split(" ", 1)
        # print(op)
        implementHeap(arr, op)
