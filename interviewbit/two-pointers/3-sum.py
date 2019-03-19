#!/usr/bin/python3

"""
Given an array S of n integers, find three integers in S such
that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""


class Solution:
    # @param arr : list of integers
    # @param K : integer
    # @return an integer
    def threeSumClosest(self, arr, K):
        arr.sort()
        # print(arr)
        ans = (1 << 31) - 1
        result = 0
        i = 0
        for i in range(0, len(arr)-2):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                three_sum = arr[i] + arr[j] + arr[k]
                if abs(K - three_sum) < ans:
                    ans = abs(K - three_sum)
                    result = three_sum
                # if three_sum == K:
                #     return ans
                elif three_sum < K:
                    j += 1
                else:
                    k -= 1
        return result
