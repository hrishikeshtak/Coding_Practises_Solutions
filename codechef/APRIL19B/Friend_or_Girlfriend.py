#!/usr/bin/python3

P = 101  # prime number
K = int(1e9 + 7)
powers = []  # store powers of prime numbers


def store_powers(M):
    # store powers of prime number from 1 to M
    global powers
    for i in range(0, M+1):
        powers.append(a_power_b(P, i))


def a_power_b(A, B):
    ans = 1
    x = A
    while B:
        if B & 1:
            ans = ((ans % K) * (x % K)) % K
        x = x * x
        B = B >> 1
    return ans


def rabin_karp_string_matching(A, B):
    M = len(A)
    N = len(B)
    A_hash = 0
    B_hash = 0

    # calculate A Hash and first window of B Hash
    for i in range(M):
        A_hash += ord(A[i]) * powers[M-i]
        A_hash = A_hash % K
        B_hash += ord(B[i]) * powers[M-i]
        B_hash = B_hash % K
    # print(A_hash)
    # print(B_hash)

    occurrences = 0
    for i in range(0, N-M+1):
        if A_hash == B_hash:
            occurrences += 1
            # # check for characters
            # for j in range(M):
            #     if B[i+j] != A[j]:
            #         break
            # j += 1
            # if j == M:
            #     occurrences += 1
            #     # print("Pattern found at index ", str(i))
        if i < N-M:
            # recalculate B hash value after sliding
            B_hash = ((B_hash - (ord(B[i]) * powers[M]) +
                      ord(B[i+M])) * P) % K
            # modulo divison over - might be -ve
            if B_hash < 0:
                B_hash = (B_hash + K) % K
            # print(B_hash)
    return occurrences


def no_of_substrings(txt, pat, N):
    cnt = 0
    for i in range(0, N):
        N = len(txt[i:])
        if rabin_karp_string_matching(pat, txt[i:]) >= 0:
            cnt += N - (txt[i:].find(pat))
            # print(txt[i:], cnt)
    return cnt


if __name__ == '__main__':
    store_powers(int(1))
    for _ in range(int(input())):
        N = int(input())
        txt, pat = input().split()
        print(no_of_substrings(txt, pat, N))
