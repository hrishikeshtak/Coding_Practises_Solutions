#!/usr/bin/python3

"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected
output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_array(arr):
    # Take 2 array: Prefix Product and Suffix Product
    N = len(arr)
    prefix_product = [0] * N
    suffix_product = [0] * N

    print("arr: ", arr)
    # Take Prefix Product
    prefix_product[0] = arr[0]
    for i in range(1, N):
        prefix_product[i] = prefix_product[i-1] * arr[i]
    print("prefix_product: ", prefix_product)

    # Take Suffix Product
    suffix_product[N-1] = arr[N-1]
    for i in range(N-2, -1, -1):
        suffix_product[i] = suffix_product[i+1] * arr[i]
    print("suffix_product: ", suffix_product)

    for i in range(0, N):
        # first element
        if i - 1 < 0:
            arr[i] = 1 * suffix_product[i + 1]
        elif i + 1 == N:
            arr[i] = prefix_product[i-1] * 1
        else:
            arr[i] = prefix_product[i-1] * suffix_product[i+1]
    return (arr)


arr = [1, 2, 3, 4, 5]
arr = [3, 2, 1]
print(product_array(arr))
