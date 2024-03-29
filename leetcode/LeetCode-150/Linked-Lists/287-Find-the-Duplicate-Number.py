"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow


if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))
