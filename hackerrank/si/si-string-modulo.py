#!/usr/bin/python3


def string_modulo(N, P):
    res = 0
    for i in range(len(N)):
        res = ((res * 10) + int(N[i])) % int(P)
    return res


if __name__ == '__main__':
    for _ in range(int(input())):
        N, P = input().split()
        print(string_modulo(N, P))
