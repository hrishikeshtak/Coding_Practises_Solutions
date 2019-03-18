#!/usr/bin/python3


def number_of_gifts(arr, n, k):
    # sort + 2-ptr technique
    arr.sort()
    remaining = []
    pair = 0
    i = 0
    j = n-1
    while i < j:
        if (arr[i] + arr[j]) % k == 0:
            i += 1
            j -= 1
            pair += 1
        else:
            remaining.append(arr[i])
            i += 1
    if i == j:
        remaining.append(arr[i])

    # find pairs from remaining arr with % k == 0
    N = len(remaining)
    # ignore already used index
    ignore_index = []
    for i in range(0, N-1):
        if i in ignore_index:
            continue
        for j in range(i+1, N):
            if j in ignore_index:
                continue
            if (arr[i] + arr[j]) % k == 0:
                pair += 1
                ignore_index.append(i)
                ignore_index.append(j)

    return 2 * pair


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(number_of_gifts(arr, n, k))
