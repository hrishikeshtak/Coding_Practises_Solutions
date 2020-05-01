#!/usr/bin/python3

"""
Product of Array Except Self

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of
any prefix or suffix of the array (including the whole array)
fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
"""


class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        # prefix array with prefix product of elements except i
        # suffix array with suffix product of elements except i

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        output = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        # print(f"prefix: {prefix}")

        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        # print(f"suffix: {suffix}")
        for i in range(0, n):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == n-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]

        return output


if __name__ == '__main__':
    # arr = [1, 2, 3, 4]
    # print(f"{Solution().productExceptSelf(arr)}")
    # arr = [2, 3, 5, 6]
    # print(f"{Solution().productExceptSelf(arr)}")
    arr = [4, 3, 2, 1, 2]
    print(f"{Solution().productExceptSelf(arr)}")
