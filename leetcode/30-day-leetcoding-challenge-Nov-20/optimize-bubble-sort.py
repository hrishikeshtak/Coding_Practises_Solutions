#!/usr/bin/python3


def bubble_sort(arr, N):
    print(f"Before Sort: {arr}")

    already_sorted = False
    for i in range(N-1, -1, -1):
        print(arr)
        if not already_sorted:
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    already_sorted = False
                else:
                    already_sorted = True
        else:
            break

    print(f"After Sort: {arr}")


if __name__ == '__main__':
    # arr = [5, 4, 3, 2, 1]
    arr = [1, 2, 3, 4, 5]
    # arr = [1, 2, 3, 5, 4]
    bubble_sort(arr, len(arr))
