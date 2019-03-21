#!/usr/bin/python3

"""
Given an array of integers and a window size K,
find the number of distinct elements in every window of
size K of the given array.
"""


def distinct_element_in_window(arr, N, K):
    hashmap = dict()
    # first add K elements to hashmap
    for i in range(0, K):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] += 1
    # now remove i - k element from hashmap and
    # add new element
    for i in range(K, N):
        # print length of distinct element in window size
        # print(hashmap)
        print(len(hashmap), end=" ")
        # decrease count of i-K element from hashmap
        # if count reach to 0 then remove that element
        hashmap[arr[i-K]] -= 1
        if hashmap[arr[i-K]] == 0:
            _ = hashmap.pop(arr[i-K])
        # add new element
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] += 1
    # print(hashmap)
    print(len(hashmap), end=" ")


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        distinct_element_in_window(arr, N, K)
        print()
