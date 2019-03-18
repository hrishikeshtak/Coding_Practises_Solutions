#!/usr/bin/python3

# find max element


def selection_sort(arr, n):
    for i in range(n-1, 0, -1):
        max_ele = i
        for j in range(i, -1, -1):
            if arr[j] >= arr[max_ele]:
                max_ele = j
        arr[i], arr[max_ele] = arr[max_ele], arr[i]
        # print(arr, max_ele, i)
        print(max_ele, end=" ")


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        selection_sort(arr, n)
        print()
