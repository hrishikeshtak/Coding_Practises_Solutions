
"""
Reverse bits of an 32 bit unsigned integer
"""


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        count = 31
        reverse_num = 0
        while A:
            reverse_num = reverse_num ^ (A & 1)
            A >>= 1
            count -= 1
            reverse_num <<= 1
        reverse_num <<= count
        return reverse_num
