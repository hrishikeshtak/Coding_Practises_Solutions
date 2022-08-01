"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res
        # Time: O(n)
        # Space: O(1)

    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        n = len(nums)
        left_prefix = [1] * n
        right_prefix = [1] * n

        left_prefix[0] = nums[0]
        right_prefix[-1] = nums[-1]

        for i in range(1, n):
            left_prefix[i] = left_prefix[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            right_prefix[i] = right_prefix[i+1] * nums[i]

        output = [1] * n
        for i in range(0, n):
            if i == 0:
                output[i] = right_prefix[i+1]
            elif i == n-1:
                output[i] = left_prefix[i-1]
            else:
                output[i] = left_prefix[i-1] * right_prefix[i+1]
        return output
        # Time: O(n)
        # Space: O(n)


if __name__ == '__main__':
    nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    print(f"nums: {nums}")
    output = Solution().productExceptSelf(nums)
    print(f"output: {output}")
