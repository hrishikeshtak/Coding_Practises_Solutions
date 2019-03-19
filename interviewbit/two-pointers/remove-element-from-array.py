"""
Given an array and a value, remove all the instances of that
value in the array.
Also return the number of elements left in the array after the
peration.
It does not matter what is left beyond the expected length.

If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        j = 0
        for i in range(0, len(A)):
            if A[i] != B:
                A[j] = A[i]
                j += 1
        # print(A[:j])
        return j
