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
    def num_square_sum(self, n):
        square_sum = 0
        while n:
            square_sum += (n % 10) * (n % 10)
            n = int(n / 10)
        return square_sum

    def isHappy(self, N):
        """
        :type n: int
        :rtype: bool
        """
        slow = N
        fast = N

        while True:
            slow = self.num_square_sum(slow)
            fast = self.num_square_sum(self.num_square_sum(fast))

            if slow != fast:
                continue
            else:
                break

        return slow == 1


if __name__ == '__main__':
    N = 20
    result = Solution().isHappy(N)
    if result:
        print("Happy")
    else:
        print("Not Happy")
