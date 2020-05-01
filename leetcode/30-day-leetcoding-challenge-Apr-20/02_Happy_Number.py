#!/usr/bin/python3

"""
Happy Number
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not
include 1. Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution(object):
    def isHappy(self, N):
        """
        :type n: int
        :rtype: bool
        """
        numbers = set()
        if N < 1:
            return False

        while True:
            square_sum = 0
            while N:
                square_sum += (N % 10) * (N % 10)
                N = int(N / 10)
            N = square_sum
            if N == 1:
                return True
            if N in numbers:
                return False
            numbers.add(N)


if __name__ == '__main__':
    N = 5555
    result = Solution().isHappy(N)
    if result:
        print("Happy")
    else:
        print("Not Happy")
