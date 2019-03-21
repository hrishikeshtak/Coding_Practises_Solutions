#!/usr/bin/python3


def intersection_union(A, B):
    intersect = set()
    union = set(A)
    for i in range(len(B)):
        if B[i] in union:
            intersect.add(B[i])
        else:
            union.add(B[i])
    print("union: ", union)
    print("intersection: ", intersect)


A = [-1, 10, 2, 18, 12, 25]
B = [6, 12, -3, 10, 23]
intersection_union(A, B)
