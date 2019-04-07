#!/usr/bin/python3

"""
Shlok and Sachin are good friends. Shlok wanted to test Sachin,
so he wrote down a string [Math Processing Error] with length
[Math Processing Error] and one character [Math Processing Error].
He wants Sachin to find the number of different substrings of
[Math Processing Error] which contain the character [Math Processing Error]
at least once. Sachin is busy with his girlfriend, so he needs you to find
the answer.
"""


def no_of_substrings(txt, pat, N):
    cnt = 0
    for i in range(0, N+1):
        for j in range(i+1, N+1):
            print(txt[i:j], txt[j-1])
            if pat in txt[i:j]:
                cnt += 1

    return cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        txt, pat = input().split()
        print(no_of_substrings(txt, pat, N))
