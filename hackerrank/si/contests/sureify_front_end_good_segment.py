#!/usr/bin/python3


# Good segment
def good_segments(arr, l, r):
    # return length of longest good segments
    # if arr is Empty
    if not arr:
        return r - l + 1

    arr.sort()
    print(arr)
    N = len(arr)
    good_segments = [[l, r]]
    max_length = 0
    j = 0
    for i in range(0, N):
        print("good_segments: ", good_segments)
        # within range
        if arr[i] < good_segments[j][1]:
            temp = good_segments[j][1]
            good_segments[j][1] = arr[i] - 1
            # add new range
            good_segments.append([arr[i]+1, temp])
            j += 1
        else:
            break

    print("good_segments: ", good_segments)
    for i in range(0, len(good_segments)):
        cur_length = good_segments[i][1] - good_segments[i][0] + 1
        max_length = max(max_length, cur_length)
    return max_length


if __name__ == '__main__':
    l = 1
    r = 7
    # bad_numbers = [37, 7, 22, 15, 49, 60]
    bad_numbers = [1, 5, 22, 15, 49, 600]
    bad_numbers = [2, 3, 4, 5]
    print(good_segments(bad_numbers, l, r))
