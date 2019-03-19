#!/usr/bin/python3


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        sign = 1
        if A < 0:
            sign = -1
            A = abs(A)
        lo = 1
        hi = A

        ans = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= A:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return sign * ans


if __name__ == '__main__':
    N = 25
    print(Solution().sqrt(N))
