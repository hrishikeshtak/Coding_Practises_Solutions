#!/usr/bin/python3

import math

M = int(1e9 + 7)


# def get_min_max_index(n):
#     """return min_index, max_index, set_bit position."""
#     if n == 1:
#         return 1, 1, 1

#     for i in range(1, n+1):
#         max_index = (i * (i + 1)) // 2
#         min_index = (max_index - i) + 1
#         if min_index <= n <= max_index:
#             return min_index, max_index, i


def a_power_b(a, b):
    # x = int(a % M)
    # b = int(b % M)
    x = a
    ans = 1

    while b != 0:
        if b & 1:
            ans = ((ans % M) * (x % M)) % M
        x = ((x % M) * (x % M)) % M
        b >>= 1
    return int(ans % int(M))


def get_min_max_index(n):
    """return max_index, set_bit position.
    (x * (x-1))/2 < n
    convert it into equation = (-1 + sqrt(q + 8n)) / 2
    """
    set_bit_pos = math.ceil((-1 + math.sqrt(8*n)) / 2)
    max_index = (set_bit_pos * (set_bit_pos + 1)) // 2
    return max_index, set_bit_pos


def two_set_bits(n):
    max_index, set_bit_pos = get_min_max_index(n)
    # print(max_index, set_bit_pos)

    # this step gives error for long data > 1023
    # OverflowError: int too large to convert to float
    # ans = (1 << set_bit_pos) | (1 << i)
    x = a_power_b(2, set_bit_pos)
    y = a_power_b(2, (set_bit_pos - (max_index - n)) - 1)
    return int(((x % M) + (y % M)) % M)


if __name__ == "__main__":
    for _ in range(int(input())):
        print(two_set_bits(int(input())))
