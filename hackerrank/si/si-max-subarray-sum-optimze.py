#!/usr/bin/python3

# optimized = O(N)
INT_MIN = -(1 << 31)


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        N = len(A)
        cur_sum = 0
        max_sum = INT_MIN

        for i in range(0, N):
            cur_sum += A[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(A))
