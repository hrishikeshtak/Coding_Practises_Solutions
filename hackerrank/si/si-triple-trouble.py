#!/usr/bin/python3


def triple_trouble(arr):
    res = 0
    for bit in range(0, 32):
        ans = 0
        for i in arr:
            # check bit is set or not
            if (i & (1 << bit)) != 0:
                ans += 1
        if ans % 3 != 0:
            res |= (1 << bit)
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(triple_trouble(arr))
