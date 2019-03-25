#!/usr/bin/python3

# Optimized - 3 O(M + NLogN)
# Using Binary Search
INT_MAX = (1 << 31) - 1


def compare(A, B):
    for i in range(0, 26):
        if B[i] < A[i]:
            return False
    return True


def valid(B, frequency_A, N, mid):
    # Rolling hash technique
    frequency_B = [0] * 26

    for i in range(0, mid):
        frequency_B[ord(B[i]) - ord('a')] += 1

    if compare(frequency_A, frequency_B):
        return True

    for i in range(mid, N):
        frequency_B[ord(B[i]) - ord('a')] += 1
        frequency_B[ord(B[i-mid]) - ord('a')] -= 1
        if compare(frequency_A, frequency_B):
            return True
    return False


def enclosing_substring(A, B):
    M = len(A)
    N = len(B)
    ans = INT_MAX

    frequency_A = [0] * 26
    for i in range(0, M):
        frequency_A[ord(A[i]) - ord('a')] += 1
    # print(A)
    # print(frequency_A)

    lo = M
    hi = N
    while lo <= hi:
        mid = (lo + hi) // 2
        if valid(B, frequency_A, N, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    if ans == INT_MAX:
        ans = -1
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = input().split()
        print(enclosing_substring(A, B))
