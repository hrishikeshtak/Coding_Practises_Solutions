#!/usr/bin/python3


def sum_of_2_numbers(arr, N):
    # if sum is odd then not possible
    s = sum(arr)
    # print(s)
    if s & 1 != 0:
        return "No"
    seq = set(arr)
    s = s // 2
    for i in range(0, N):
        if (s - arr[i]) in seq:
            return "Yes"
    return "No"


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(sum_of_2_numbers(arr, N))
