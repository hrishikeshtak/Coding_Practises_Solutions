#!/usr/bin/python3

"""Maximum Subarray"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = 0
        max_sum = 0
        for i in nums:
            if _sum + i <= 0:
                _sum = 0
            else:
                _sum = _sum + i
            max_sum = max(max_sum, _sum)

        if max_sum == 0 and 0 not in nums:
            return max(nums)

        return max_sum


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-1,-2,-3,-4]
    # arr = [-1, 1, 2, 1]
    res = Solution().maxSubArray(arr)
    print(f"result: {res}")
