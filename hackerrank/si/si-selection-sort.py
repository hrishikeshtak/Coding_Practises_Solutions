#!/usr/bin/python3


def selection_sort(arr, n):
    for i in range(n-1):
        min_ele = i
        for j in range(i+1, n):
            if arr[j] <= arr[min_ele]:
                min_ele = j
        arr[i], arr[min_ele] = arr[min_ele], arr[i]
        # print(arr, min_ele, i)
        print(min_ele, end=" ")


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        selection_sort(arr, n)
        print()
