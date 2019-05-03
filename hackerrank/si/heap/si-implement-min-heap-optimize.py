#!/usr/bin/python3

# 0 based index


def insert(arr, key):
    arr.append(key)

    # after addition, check heap property
    idx = len(arr) - 1

    while idx > 0 and arr[idx] < arr[(idx-1)//2]:
        arr[idx], arr[(idx-1)//2] = arr[(idx-1)//2], arr[idx]
        idx = ((idx-1) // 2)


def getMin(arr):
    N = len(arr)
    if N == 0:
        print("Empty")
        # stdout.write(str("Empty") + "\n")
    else:
        print(arr[0])
        # stdout.write(str(arr[1]) + "\n")


def delMin(arr):
    # print("before delMin: ")
    # print(arr)

    # copy last element to 1st element and then maintain heap property
    N = len(arr)
    if N == 0:
        return
    elif N == 1:
        _ = arr.pop()
        return

    arr[0] = arr.pop()
    heapify_recursive(arr, 0, len(arr))
    # print("After delMin: ")
    # print(arr)


def heapify_recursive(arr, idx, N):
    smallest = idx
    left = 2*idx + 1
    right = 2*idx + 2

    # find min index from l and r
    if left < N and arr[left] < arr[smallest]:
        smallest = left
    if right < N and arr[right] < arr[smallest]:
        smallest = right

    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        heapify_recursive(arr, smallest, N)


def implementHeap(arr, op):
    if op[0].lower() == "insert":
        x = int(op[1])
        # x = int(op[1])
        insert(arr, x)

    elif op[0].lower() == "getmin":
        getMin(arr)

    elif op[0].lower() == "delmin":
        delMin(arr)
    else:
        print("Invalid Operation")
        return


if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        # op = stdin.readline().split(" ", 1)
        op = input().split(" ", 1)
        # print(op)
        implementHeap(arr, op)
