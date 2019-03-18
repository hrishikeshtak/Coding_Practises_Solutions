#!/usr/bin/python3


def search(txt, pat):
    N = len(txt)
    M = len(pat)

    for i in range(0, N-M+1):
        j = 0

        for j in range(0, M):
            if txt[i+j] != pat[j]:
                break
        if j == M - 1:
            print("Pattern found at index ", i)


if __name__ == '__main__':
    txt = "THIS IS A TEST TEXT"
    pat = "TEST"
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(txt, pat)
