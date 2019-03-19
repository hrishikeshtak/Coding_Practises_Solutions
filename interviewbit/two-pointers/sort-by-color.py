"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the
color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""


class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        lo = 0
        mid = 0
        hi = len(A) - 1
        while mid <= hi:
            if A[mid] == 0:
                A[lo], A[mid] = A[mid], A[lo]
                lo += 1
                mid += 1
            elif A[mid] == 1:
                mid += 1
            else:
                A[mid], A[hi] = A[hi], A[mid]
                hi -= 1
        return A
