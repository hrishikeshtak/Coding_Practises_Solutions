#!/usr/bin/python3


def ToH(N, src, temp, dest):
    if N == 0:
        return

    ToH(N-1, src, dest, temp)
    print("Move {} from {} to {}".format(N, src, dest))
    ToH(N-1, temp, src, dest)


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        # Total moves = 2**N - 1
        print((1 << N) - 1)
        ToH(N, 'A', 'B', 'C')
