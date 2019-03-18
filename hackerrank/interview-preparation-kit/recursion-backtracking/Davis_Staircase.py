#!/usr/bin/python3


def num_ways_X(N, X):
    if N == 0:
        return 1
    nums = [0] * (N+1)
    nums[0] = 1
    for i in range(1, N+1):
        total = 0
        for j in X:
            if i - j >= 0:
                total += nums[i-j]
        nums[i] = total
    # print(nums)
    return nums[N]


if __name__ == "__main__":
    for _ in range(int(input())):
        # number of ways he can climb staircase
        X = {1, 2, 3}
        N = int(input())
        print(num_ways_X(N, X))
