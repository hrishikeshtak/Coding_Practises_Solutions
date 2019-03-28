#!/usr/bin/python3

"""
This method doesn’t cause overflow, but it doesn’t tell
which one occurs twice and which one is missing.
We can add one more step that checks which one is
missing and which one is repeating. This can be easily
done in O(n) time.
"""
from functools import reduce


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, arr):
        N = len(arr)
        xor = reduce(lambda x, y: x ^ y, arr)
        for i in range(1, N+1):
            xor ^= i

        # this will contains only set bits of repeated numbers
        set_bit_number = xor & ~(xor - 1)
        # print("set_bit_number: ", set_bit_number)
        # print("xor2: ", xor2)
        x = 0
        y = 0
        # xor with xor2 and those who are having set bits from arr
        for i in arr:
            if i & set_bit_number:
                x ^= i
            else:
                y ^= i
        for i in range(1, N+1):
            if i & set_bit_number:
                x ^= i
            else:
                y ^= i
        # this method doesn't tell which one is occurs twice and
        # which one missing
        # To check which one is missing
        if x in arr:
            return (x, y)
        else:
            return (y, x)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x, y = Solution().repeatedNumber(arr)
    print(x, y)
