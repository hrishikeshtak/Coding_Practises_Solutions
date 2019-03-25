#!/usr/bin/python3

# Optimized - 1 O(M + N^3)
INT_MAX = (1 << 31) - 1


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
        for j in range(i, N+1):
            frequency_B = [0] * 26
            if (j - i) >= M:
                for k in range(i, j):
                    frequency_B[ord(B[k]) - ord('a')] += 1
                # print(frequency_B)
                # compare frequency of A and B
                if compare(frequency_A, frequency_B):
                    ans = min(ans, j - i)

    if ans == INT_MAX:
        ans = -1
    return ans


def compare(A, B):
    for i, j in zip(B, A):
        if i < j:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = input().split()
        print(enclosing_substring(A, B))
