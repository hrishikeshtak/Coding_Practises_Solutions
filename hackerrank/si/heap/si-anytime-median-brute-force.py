#!/usr/bin/python3

# using Insertion sort


def anytime_median(arr, N):
    for i in range(0, N):
        temp = arr[i]
        j = i
        while j >= 1 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
        print(arr[i//2], end=" ")


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        anytime_median(arr, N)
        print()
