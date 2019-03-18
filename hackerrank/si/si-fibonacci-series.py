#!/usr/bin/python3


def num_ways(n):
    if n == 0 or n == 1:
        return 1
    nums = [0] * (n + 1)
    nums[0] = nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
        print(nums)
    return nums[n]


if __name__ == "__main__":
    n = 4
    print(num_ways(n))
