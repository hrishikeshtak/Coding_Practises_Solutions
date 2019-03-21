#!/usr/bin/python3

"""
Polycarp plays "Game 23". Initially he has a number n and his
goal is to transform it to m. In one move, he can multiply n
by 2 or multiply n by 3. He can perform any number of moves.

Print the number of moves needed to transform n to m. Print -1
if it is impossible to do so.
"""


def game23(N, M):
    print(N)
    if N == M:
        return 0
    elif N > M:
        return -1
    a = b = 0
    a += 1 + game23(N*2, M)
    b += 1 + game23(N*3, M)
    print("a: %s, b: %s" % (a, b))
    if a != -1 and b == -1:
        return a
    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(game23(N, M))
