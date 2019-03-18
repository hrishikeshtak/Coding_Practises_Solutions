#!/usr/bin/python3


def consecutive_set_bits(N):
    count = 0
    while N != 0:
        N = N & (N << 1)
        count += 1
    return count


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(consecutive_set_bits(N))
