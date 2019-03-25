#!/usr/bin/python3

# Optimized - 2 O(M + N^2)
INT_MAX = (1 << 31) - 1


def compare(A, B):
    for i in range(0, 26):
        if B[i] < A[i]:
            return False
    return True


def enclosing_substring(A, B):
    M = len(A)
    N = len(B)
    ans = INT_MAX

    frequency_A = [0] * 26
    for i in range(0, M):
        frequency_A[ord(A[i]) - ord('a')] += 1
    # print(A)
    # print(frequency_A)

    for i in range(0, N+1):
        frequency_B = [0] * 26
        for j in range(i, N):
            frequency_B[ord(B[j]) - ord('a')] += 1
            # print(frequency_B)
            # compare frequency of A and B
            if compare(frequency_A, frequency_B):
                ans = min(ans, j - i + 1)

    if ans == INT_MAX:
        ans = -1
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = input().split()
        print(enclosing_substring(A, B))
