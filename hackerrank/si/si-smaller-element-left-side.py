#!/usr/bin/python3

# Find 1st smaller elements on left side


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        N = len(arr)
        s = [-1] * N
        b = [-1] * N
        top = -1
        top += 1
        s[top] = 0

        for i in range(1, N):
            # print("stack: ", s)
            # print("b: ", b)
            while top >= 0:
                if arr[i] > arr[s[top]]:
                    b[i] = arr[s[top]]
                    top += 1
                    s[top] = i
                    break
                else:
                    top -= 1
            if top == -1:
                b[i] = -1
                top += 1
                s[top] = i
        return b


if __name__ == '__main__':
    A = [4, 5, 2, 10, 8]
    A = [3, 2, 1]
    A = [39, 27, 11, 4, 24, 32, 32, 1]
    print(Solution().prevSmaller(A))
