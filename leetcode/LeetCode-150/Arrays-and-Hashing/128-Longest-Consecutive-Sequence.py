"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums to find out the start of seq
        numSet = set(nums)

        max_length = 0
        for num in nums:
            # find out the start of seq by checking (num - 1) exists in hashset,
            # if exists then that is not start of seq,
            # if does not exists then that num is start of seq
            if (num - 1) not in numSet:
                # found the start of seq
                # print(f"start_seq: {num}")
                length = 0
                while num + length in numSet:
                    # check next num is in set
                    length += 1
                max_length = max(length, max_length)
        return max_length


if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    print(f"{Solution().longestConsecutive(nums)}")
