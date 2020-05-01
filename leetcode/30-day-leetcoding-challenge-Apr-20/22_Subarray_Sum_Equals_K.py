#!/usr/bin/python3

"""
Subarray Sum Equals K
"""

# # brute force
# class Solution:
#     def subarraySum(self, nums: 'List[int]', k: int) -> int:

#         count = 0
#         for i in range(0, len(nums)):
#             _sum = 0
#             for j in range(i, len(nums)):
#                 _sum += nums[j]
#                 if _sum == k:
#                     count += 1

#         return count



# optimize O(n)


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:

        prev_sum = defaultdict(lambda: 0)
        cur_sum = 0
        res = 0

        for i in range(0, len(nums)):
            cur_sum += nums[i]

            if cur_sum == k:
                res += 1

            if (cur_sum - k) in prev_sum:
                res += prev_sum[(cur_sum - k)]

            prev_sum[cur_sum] += 1

        return res


if __name__ == '__main__':
    # arr = [1, 1, 1, 1]
    arr = [0,0,0,0,0,0,0,0,0,0]  # ans 55
    print(f"{Solution().subarraySum(arr, 0)}")
