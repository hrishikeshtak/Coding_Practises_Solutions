#!/usr/bin/python3

# LCM and HCF (GCD)


def _gcd(A, B):
    if A == 0:
        return B
    return _gcd(B % A, A)


def lcm_and_hcf(A, B):
    # gcd
    gcd = _gcd(A, B)
    # lcm
    lcm = (A * B) // gcd
    print(lcm, gcd)


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = map(int, input().split())
        lcm_and_hcf(A, B)
