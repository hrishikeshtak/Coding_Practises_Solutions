#!/usr/bin/python3

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num):
    """Encode a positive number in Base X"""
    if num == 0:
        return ALPHABET[0]

    base = len(ALPHABET)
    slug = []

    while num:
        num, rem = divmod(num, base)
        slug.append(ALPHABET[rem])
    slug.reverse()
    return "".join(slug)


def decode(string):
    """Decode a Base X encoded string into the number"""
    base = len(ALPHABET)
    num = 0
    idx = 0
    strlen = len(string)

    for char in string:
        power = strlen - (idx + 1)
        num += ALPHABET.index(char) * (base ** power)
        idx += 1
    return num


if __name__ == '__main__':
    for i in range(100):
        print(i, encode(i), decode(encode(i)))
