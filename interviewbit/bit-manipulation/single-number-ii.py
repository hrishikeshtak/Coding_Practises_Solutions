"""
Given an array of integers, every element appears thrice except
for one which occurs once.

Find that element which does not appear thrice.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, arr):
        ans = 0
        for bit in range(31, -1, -1):
            bit_count = 0
            for i in arr:
                if self.check_bit(i, bit):
                    bit_count += 1
            # print(bit_count, bit)
            if bit_count % 3 != 0:
                ans |= (1 << bit)
        return ans

    def check_bit(self, n, i):
        return (n >> i) & 1
