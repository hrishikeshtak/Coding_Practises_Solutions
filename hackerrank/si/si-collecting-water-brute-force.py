#!/usr/bin/python3

# Brute Force
INT_MIN = -(1 << 31)


def water_collection(arr, N):
    left_highest = right_highest = INT_MIN
    count = 0
    for i in range(0, N):
        left_highest = max(left_highest, arr[i])
        # find right highest
        for j in range(i+1, N):
            right_highest = max(right_highest, arr[j])
        count += min(left_highest, right_highest) - arr[i]
        # print("left_highest: %s, right_highest: %s, index: %s, count: %s" % (
        #     left_highest, right_highest, i, count))

    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(water_collection(arr, N))
