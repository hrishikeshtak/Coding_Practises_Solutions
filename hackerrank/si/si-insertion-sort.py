#!/usr/bin/python3


def insertion_sort(arr, n):
    for i in range(1, n):
        j = i
        temp = arr[j]
        while arr[j-1] > temp and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
        # print(arr)
        print(j, end=" ")


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        insertion_sort(arr, n)
        print()
