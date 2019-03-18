#!/usr/bin/python3


def cube_root(N):
    if N == 0 or N == 1:
        return N
    # For negative number
    sign = 1
    if N < 0:
        sign = -1
        N = abs(N)
    ans = 1
    lo = 1
    hi = N

    # print(N, sign)
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid * mid == N:
            ans = mid
            break
        elif mid * mid * mid > N:
            hi = mid - 1
        else:
            lo = mid + 1
            ans = mid
    return sign * ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        print(cube_root(N))
