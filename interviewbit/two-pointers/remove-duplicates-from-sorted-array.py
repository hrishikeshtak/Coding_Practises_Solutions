class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        N = len(A)
        if N == 0 or N == 1:
            return N

        j = 0
        for i in range(0, N-1):
            if A[i] != A[i+1]:
                A[j] = A[i]
                j += 1
        A[j] = A[N-1]
        # print(A)
        return j+1


if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5, 6]
    print(A)
    print(Solution().removeDuplicates(A))
