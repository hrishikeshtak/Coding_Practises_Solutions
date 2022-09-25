"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        
        xor_res = 0
        for i in range(len(nums)+1):
            xor_res ^= i
        
        return res ^ xor_res
            
nums = [3,0,1]
print(f"missingNumber: {Solution().missingNumber(nums)}")