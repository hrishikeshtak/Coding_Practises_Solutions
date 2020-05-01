#!/usr/bin/python3

"""
Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""


class Solution:

    def msbBit(self, n):
        msb_bit = -1

        while n:
            n = n >> 1
            msb_bit += 1
        return msb_bit

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0

        while m > 0 and n > 0:
            m_msb_bit = self.msbBit(m)
            n_msb_bit = self.msbBit(n)

            # print(f"msb_bit of {m} = {m_msb_bit}")
            # print(f"msb_bit of {n} = {n_msb_bit}")

            if m_msb_bit != n_msb_bit:
                break

            msb_val = (1 << m_msb_bit)
            ans += msb_val

            m = m - msb_val
            n = n - msb_val

        return ans


if __name__ == '__main__':
    print(f"{Solution().rangeBitwiseAnd(17, 19)}")
    print(f"{Solution().rangeBitwiseAnd(5, 7)}")
