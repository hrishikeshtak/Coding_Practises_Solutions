#!/usr/bin/python3

# Find length of longest subarray, whose elements
# can be rearranged to get contiguous array.
# diff bw contiguous element must be 1


def longest_contiguous_subarray(arr, N):
    # using max and min approach
    # carry forward min and max
    ans = 1
    for i in range(0, N):
        _min = arr[i]
        _max = arr[i]
        hashset = {arr[i]}
        for j in range(i+1, N):
            _min = min(_min, arr[j])
            _max = max(_max, arr[j])
            hashset.add(arr[j])
            # if _max - _min + 1 == j - i + 1:
            if _max - _min + 1 == len(hashset):
                print(arr[i:j+1])
                ans = max(ans, j-i+1)
                # ans = max(ans, len(hashset))

    return ans


arr = [10, 15, 13, 16, 14, 9, 8, 11, 2, 6, 5, 3, 1, 4, 1, 1]
print(longest_contiguous_subarray(arr, len(arr)))
