"""
Divide two integers without using multiplication,
division and mod operator.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        sign = -1 if (A < 0) ^ (B < 0) else 1

        A = abs(A)
        B = abs(B)

        quotient = 0
        temp = 0

        for i in range(31, -1, -1):
            if temp + (B << i) <= A:
                temp += B << i
                quotient |= 1 << i

        return sign * quotient
