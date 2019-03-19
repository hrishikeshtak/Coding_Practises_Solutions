#!/usr/bin/python3

"""
1. Get all even bits by & with 0xAAAAAAAA
2. Get all odd bits by & with 0x55555555
3. right shift all even bits
4. left shift all odd bits
5. combine new even and new odd bits.
"""


def swapBits(n):
    even_bits = n & 0xAAAAAAAA
    odd_bits = n & 0x55555555

    even_bits >>= 1
    odd_bits <<= 1

    return even_bits | odd_bits


if __name__ == "__main__":
    for _ in range(int(input())):
        print(swapBits(int(input())))
