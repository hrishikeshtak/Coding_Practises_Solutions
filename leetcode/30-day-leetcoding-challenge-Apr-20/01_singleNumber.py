#!/usr/bin/python3

"""Single Number"""

from functools import reduce


class Solution(object):
    """
    Given a non-empty array of integers, every element appears
    twice except for one. Find that single one.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [2, 2, 1]
    ans = Solution().singleNumber(nums)
    print(f"nums: {nums}")
    print(f"ans: {ans}")

    nums = [4, 1, 2, 1, 2]
    ans = Solution().singleNumber(nums)
    print(f"nums: {nums}")
    print(f"ans: {ans}")
