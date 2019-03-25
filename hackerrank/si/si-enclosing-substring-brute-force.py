#!/usr/bin/python3

# Brute Force O(N^4)
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
        substring = []
        for j in range(i, N+1):
            frequency_B = [0] * 26
            # print(B[i:j])
            if len(B[i:j]) >= M:
                substring = B[i:j]
                for k in range(len(substring)):
                    frequency_B[ord(substring[k]) - ord('a')] += 1
                # print(substring)
                # print(frequency_B)
                # compare frequency of A and B
                if compare(frequency_A, frequency_B):
                    # print(substring)
                    ans = min(ans, len(substring))

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
