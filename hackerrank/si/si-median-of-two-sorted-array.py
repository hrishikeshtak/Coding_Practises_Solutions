#!/usr/bin/python3

# Using Binary Search
# only works if N + M is odd


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        N = len(A)
        M = len(B)
        if len(A) == 0:
            return B[M//2]
        elif len(B) == 0:
            return A[N//2]

        lo = min(A[0], B[0])
        hi = max(A[-1], B[-1])
        # Median position
        K = (N + M) // 2

        while lo <= hi:
            mid = (lo + hi) // 2
            # find number of element less then mid from A and B array
            less = self.floor(A, N, mid) + self.floor(B, M, mid) + 2
            if less == K:
                # check mid present in array or not
                if self.BS(A, N, mid) or self.BS(B, M, mid):
                    return mid
            if less <= K:
                lo = mid + 1
            else:
                hi = mid - 1

    def floor(self, arr, N, X):
        """Return No of elements less than X"""
        lo = 0
        hi = N - 1
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
    A = [-5, 3, 6, 12, 15]
    B = [-12, -10, -6, -3, 4, 10]
    A = []
    B = [20]
    print(Solution().findMedianSortedArrays(A, B))
