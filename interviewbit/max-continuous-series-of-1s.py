#!/usr/bin/python3


def consecutive_ones(arr, M):
    i = j = 0
    x = y = 0
    while j < len(arr):
        if arr[j] == 1:
            # update indices
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

    return(list(range(x, y+1)))


if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    M = 1
    print(consecutive_ones(arr, M))
