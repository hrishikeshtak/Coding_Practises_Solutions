"""
Given an array of integers,
every element appears twice except for one. Find that single one.
"""

from functools import reduce


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)
