#!/usr/bin/python3

"""
Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""


class Solution:
    def canJump(self, nums: 'List[int]') -> bool:

        n = len(nums)

        lastpoint = n - 1

        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastpoint:
                lastpoint = i

        return lastpoint == 0


if __name__ == '__main__':
    # A = [2, 3, 1, 1, 4]
    # A = [1]
    # A = [3, 2, 1, 0, 4]
    A = [0, 1]
    print(f"{Solution().canJump(A)}")
