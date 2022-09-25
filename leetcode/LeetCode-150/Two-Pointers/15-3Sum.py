"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # sort the array to use the two pointer technique
        nums.sort()

        for i, num in enumerate(nums):
            # this is to check if we have same start num, to avoid duplicate triplets
            if i > 0 and nums[i-1] == num:
                continue
            
            l, r = i+1, len(nums) - 1
            # [-4, -1, -1, 0, 1, 2]
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # this is to avoid duplicate numbers
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]
	print(Solution().threeSum(nums))
