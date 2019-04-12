#!/usr/bin/python3


def max_contiguous_series_of_1(arr, N, M):
    i = j = 0
    x = y = 0

    while j < N:
        if arr[j] == 1:
            if j - i > y - x:
                x, y = i, j
            j += 1
        elif arr[j] == 0 and M > 0:
            if j - i > y - x:
                x, y = i, j
            j += 1
            M -= 1
        else:
            if arr[i] == 0:
                M += 1
            i += 1
            # j += 1
    return len(list(range(x, y+1)))


if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        print(max_contiguous_series_of_1(arr, N, M))
