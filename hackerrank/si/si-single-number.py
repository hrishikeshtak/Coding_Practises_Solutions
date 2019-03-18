from functools import reduce


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)


a = [1, 2, 2, 3, 1]
print(Solution().singleNumber(a))
