#!/usr/bin/python3

import random

NUM_CHARS_IN_SLUG = 7
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def generateRandomSlug():
    result = []
    for i in range(NUM_CHARS_IN_SLUG):
        result.append(ALPHABET[random.randint(0, len(ALPHABET)-1)])

    return "".join(result)


print(generateRandomSlug())
