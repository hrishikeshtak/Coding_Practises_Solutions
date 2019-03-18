#!/usr/bin/python3


def bubble_sort(arr, n):
    swapped = True
    total_pass = 0
    passes = n-1
    while passes >= 0 and swapped:
        swapped = False
        for i in range(passes):
            if arr[i] > arr[i+1]:
                swapped = True
                total_pass += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
            # print(arr)
        passes -= 1
    return (total_pass)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(bubble_sort(arr, n))
