"""
Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum_array = [0] * n
        right_sum_array = [0] * n
        
        for i in range(1, n):
            left_sum_array[i] = left_sum_array[i-1] + nums[i-1]
        # print(f"left_sum_array: {left_sum_array}")
        
        for i in range(n-2, -1, -1):
            right_sum_array[i] = right_sum_array[i+1] + nums[i+1]
        # print(f"right_sum_array: {right_sum_array}")

        for i in range(0, n):
        	if left_sum_array[i] == right_sum_array[i]:
        		return i
        return -1


if __name__ == '__main__':
	nums = [1,7,3,6,5,6]
	nums = [1,2,3]
	nums = [2,1,-1]
	print(Solution().pivotIndex(nums))
