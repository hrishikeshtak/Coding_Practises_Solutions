#!/usr/bin/python3


def sum_and_xor(N):
    count = 0
    while N != 0:
        if N & 1 == 0:
            count += 1
        N = N >> 1
    return (1 << count) - 1


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(sum_and_xor(N))
