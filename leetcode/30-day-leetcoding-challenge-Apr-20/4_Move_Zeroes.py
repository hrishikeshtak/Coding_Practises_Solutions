#!/usr/bin/python3

"""Move Zeroes"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0  # pointing to the zeros
        j = 0  # pointing to the non-zeros

        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        print(f"result: {nums}")


if __name__ == '__main__':
    # arr = [0, 1, 0, 3, 12]
    arr = [0, 1, 0, 0, 0]
    arr = [0, 0, 0, 0, 4]
    Solution().moveZeroes(arr)
