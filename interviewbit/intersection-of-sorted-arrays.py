#!/usr/bin/python3


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        output = []
        i = 0
        j = 0

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                i += 1
            elif A[i] == B[j]:
                output.append(A[i])
                i += 1
                j += 1
            else:
                j += 1
        return output


if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5, 6]
    B = [3, 3, 5]
    # Output : [3 3 5]
    B = [3, 5]
    print(A)
    print(B)
    print(Solution().intersect(A, B))
