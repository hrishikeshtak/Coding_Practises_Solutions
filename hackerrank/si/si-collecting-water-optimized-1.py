#!/usr/bin/python3

# Pre compute Left and Right highest bar


def water_collection(arr, N):
    count = 0
    left = [0] * N
    right = [0] * N

    # store left highest
    left[0] = arr[0]
    for i in range(1, N):
        left[i] = max(left[i-1], arr[i])

    # store right highest
    right[-1] = arr[N-1]
    for i in range(N-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    # print("Left: ", left)
    # print("Right: ", right)

    for i in range(0, N):
        count += min(left[i], right[i]) - arr[i]
    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(water_collection(arr, N))
