#!/usr/bin/python3

M = int(1e9 + 7)


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        # print(A)

        # 1. mark -ve and > (N + 1) element as infinity
        for i in range(0, N):
            if A[i] <= 0 or A[i] > N:
                A[i] = M

        # print(A)
        # 2. update indices of present element
        for i in range(0, N):
            if abs(A[i]) != M and A[abs(A[i]) - 1] > 0:
                A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]
        # print(A)

        # 3. Find +ve element and return its index + 1
        # if no +ve element then return N + 1 as ans
        count = 0
        for i in range(0, N):
            if A[i] > 0 and A[i] != -M:
                return i + 1
            elif A[i] == M:
                count += 1
        if count == N:
            return 1
        else:
            return N + 1


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(Solution().firstMissingPositive(arr))
