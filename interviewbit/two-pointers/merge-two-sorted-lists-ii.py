class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                i += 1
            else:
                A.insert(i, B[j])
                j += 1
        while j < len(B):
            A.append(B[j])
            j += 1
        A = list(map(str, A))
        print(" ".join(A) + " ")


if __name__ == "__main__":
    A = [1, 5, 8]
    B = [6, 9]
    A = [-4, 3]
    B = [-2, -2]
    print(A)
    print(B)
    Solution().merge(A, B)
