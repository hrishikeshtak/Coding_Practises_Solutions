"""
Write a function that takes an unsigned integer and returns
the number of 1 bits it has.
"""


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A != 0:
            count += (A & 1)
            A = A >> 1
        return count
