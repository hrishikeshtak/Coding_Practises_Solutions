#!/usr/bin/python3

"""
Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: 'List[int]') -> int:
        max_length = 0
        cur_sum = 0
        # store sum with index as key/value pair
        hash_map = {}

        # update 0 as -1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        # Consider all 0 values as -1. The problem now reduces to find out
        # the maximum length subarray with sum = 0.
        for i in range(0, len(nums)):
            cur_sum += nums[i]

            if cur_sum == 0:
                max_length = i + 1

            if cur_sum in hash_map:
                if max_length < i - hash_map[cur_sum]:
                    max_length = i - hash_map[cur_sum]
            else:
                hash_map[cur_sum] = i

        return max_length


if __name__ == '__main__':
    nums = [0, 1, 0, 0, 0, 1, 1, 1]
    nums = [1, 0, 1, 1]
    nums = [0, 0, 1, 0, 0, 0, 1, 1]
    print(f"{Solution().findMaxLength(nums)}")
