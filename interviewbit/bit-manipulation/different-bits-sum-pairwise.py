"""
We define f(X, Y) as number of different corresponding bits in
binary representation of X and Y. For example, f(2, 7) = 2,
since binary representation of 2 and 7 are 010 and 111, respectively.
The first and the third bit differ, so f(2, 7) = 2.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, arr):
        ans = 0
        n = len(arr)
        for bit in range(0, 32):
            count = 0
            # get total no whose ith bit is set
            for i in arr:
                if i & (1 << bit):
                    count += 1
            # there are n-count pairs whose ith bit is unset
            ans += count * (n - count) * 2
        return int(ans % (1e9 + 7))
