#!/usr/bin/python3


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    seq = [0]*(n+1)

    for _ in range(m):
        x, y, incr = [int(i) for i in input().split()]
        seq[x-1] += incr
        # for y index do subtract
        if (y) <= len(seq):
            seq[y] -= incr
        # print(seq)
    max = x = 0
    for i in seq:
        x = x + i
        if max < x:
            max = x
    print(max)
