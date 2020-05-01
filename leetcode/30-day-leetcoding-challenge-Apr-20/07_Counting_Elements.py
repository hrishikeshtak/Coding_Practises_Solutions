#!/usr/bin/python3

"""
Counting Elements.
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

"""


class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in arr:
            if i+1 in arr:
                count += 1

        return count


if __name__ == '__main__':
    arr = [1, 1, 3, 3, 5, 5, 7, 7]
    print(f"output: {Solution().countElements(arr)}")
    arr = [1, 2, 3]
    print(f"output: {Solution().countElements(arr)}")
    arr = [1, 3, 2, 3, 5, 0]
    print(f"output: {Solution().countElements(arr)}")
    arr = [1, 1, 2, 2]
    print(f"output: {Solution().countElements(arr)}")
