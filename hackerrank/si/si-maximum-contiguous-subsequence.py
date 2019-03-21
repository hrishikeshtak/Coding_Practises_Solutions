#!/usr/bin/python3

# using Hashing O(N)


def max_contiguous_subsequence(arr, N):
    subseq = set()
    # Hash all elements
    for i in range(N):
        if arr[i] not in subseq:
            subseq.add(arr[i])

    # print(subseq)
    ans = -(1 << 31)
    for i in range(0, N):
        # check the element is a start point or not
        if (arr[i] - 1) not in subseq:
            j = arr[i]
            # check increasing series in set
            while j in subseq:
                j += 1

            # update ans
            ans = max(ans, j - arr[i])

    return ans


for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_contiguous_subsequence(arr, N))
