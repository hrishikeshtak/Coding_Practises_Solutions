#!/usr/bin/python3

"""
Given a N cross M matrix in which each row is sorted,
find the overall median of the matrix. Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
"""

INT_MIN = -(1 << 31)
INT_MAX = (1 << 31) - 1


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        # print(A)
        N = len(A)
        M = len(A[0])

        K = (N * M) // 2
        # Odd condition
        if (N * M) % 2 != 0:
            m1 = self.median(A, N, M, K)
            return m1

    def median(self, A, N, M, K):
        # find lo (min) element from matrix
        lo = INT_MAX
        for arr in A:
            lo = min(lo, arr[0])

        # find hi (max) element from matrix
        hi = INT_MIN
        for arr in A:
            hi = max(hi, arr[-1])

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print("lo: %s, mid: %s, hi: %s, K: %s" % (lo, mid, hi, K))
            # find number of element less then mid from A and B array
            less = 0
            for arr in A:
                less += self.floor(arr, M, mid) + 1
            # print("less: %s" % (less))
            if less == K:
                # check mid present in matrix or not
                for arr in A:
                    if self.BS(arr, M, mid):
                        ans = mid
                        break
            if less <= K:
                # store mid value, this will useful in case of
                # duplicate element
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

    def floor(self, arr, N, X):
        """Return No of elements less than X"""
        lo = 0
        hi = N - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(lo, mid, hi)
            if arr[mid] < X:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def BS(self, arr, N, X):
        """Search X in arr"""
        lo = 0
        hi = N - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == X:
                return True
            elif arr[mid] < X:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == '__main__':
    A = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    A = [[2], [1], [4], [1], [2], [2], [5]]
    print(Solution().findMedian(A))
