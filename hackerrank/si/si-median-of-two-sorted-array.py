#!/usr/bin/python3

# Using Binary Search
# only works if N + M is odd
# Updated to work with both even and odd length
# Failed with duplicate elements


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        N = len(A)
        M = len(B)
        if len(A) == 0 and (N + M) % 2 == 0:
            return (B[M//2] + B[(M//2)-1]) / 2.0
        elif len(A) == 0:
            return B[M//2]
        elif len(B) == 0 and (N + M) % 2 == 0:
            return (A[N//2] + A[(N//2)-1]) / 2.0
        elif len(B) == 0:
            return A[N//2]

        # Median position, if N + M is odd
        K = (N + M) // 2
        # Odd condition
        if (N + M) % 2 != 0:
            m1 = self.median(A, B, N, M, K)
            return m1
        # even condition
        else:
            m1 = self.median(A, B, N, M, K)
            m2 = self.median(A, B, N, M, K-1)
            # print("m1: %s, m2: %s" % (m1, m2))
            return (m1 + m2) / 2.0

    def median(self, A, B, N, M, K):
        lo = min(A[0], B[0])
        hi = max(A[-1], B[-1])

        while lo <= hi:
            mid = (lo + hi) // 2
            # print("lo: %s, mid: %s, hi: %s, K: %s" % (lo, mid, hi, K))
            # find number of element less then mid from A and B array
            less = self.floor(A, N, mid) + self.floor(B, M, mid) + 2
            # print("less: %s" % (less))
            if less == K:
                # check mid present in array or not
                if self.BS(A, N, mid) or self.BS(B, M, mid):
                    return mid
            if less <= K:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1

    def floor(self, arr, N, X):
        """Return No of elements less than X"""
        lo = 0
        hi = N - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
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
    A = [-5, -2, 4, 18, 25]
    B = [-8, -1, 0, 7, 10, 15, 23, 31]
    # A = [-5, 3, 6, 12, 15]
    # B = [-12, -10, -6, -3, 4, 10]
    # A = []
    # B = [20]
    # A = [5, 8, 10, 20]
    # B = [900]
    # even length
    # A = [2, 3, 5, 8]
    # B = [10, 12, 14, 16, 18, 20]
    A = [-50, -41, -40, -19, 5, 21, 28]
    B = [-50, -21, -10]
    # A = [0, 23]
    # B = []
    # A = [-37, -10, -5, 5, 17, 34, 39]
    # B = [-30, -27, -21, -21, 41]
    # A = [-41, -4, 15, 17, 28, 30, 40]
    # B = [-41, -40, -35, -30, -8, 6, 6, 15, 24]
    print(Solution().findMedianSortedArrays(A, B))
