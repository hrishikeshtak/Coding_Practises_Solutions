"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # length of nums
        n = len(nums)
        # Logic: is to modify the array when we visited i then go to nums[i-1] index and mark the number
        #     as negative so that we can identify the index is already visited
        #     Then at the end traverse the entire array and find the positive numbers and return
        #     [number+1]
        for i in range(0, n):
            if nums[abs(nums[i])-1] < 0:
                continue
            else:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        # print(f"nums: {nums}")
        ans: List[int] = []
        for i in range(0, n):
            if nums[i] > 0:
                ans.append(i+1)
        # print(f"ans: {ans}")
        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
