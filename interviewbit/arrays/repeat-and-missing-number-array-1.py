#!/usr/bin/python3


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, arr):
        N = len(arr)
        x = 0  # repeated
        y = 0  # missing
        for i in range(0, N):
            if arr[abs(arr[i]) - 1] < 0:
                x = abs(arr[i])
            else:
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        for i in range(0, N):
            if arr[i] > 0:
                y = i + 1
                break
        return x, y


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x, y = Solution().repeatedNumber(arr)
    print(x, y)
