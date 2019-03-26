#!/usr/bin/python3

"""
As you might already know, Ada the Ladybug is a farmer.
She has a long alley of trees. She wants the alley to look
good so she has decided to make the heights of all trees equal.
She has two possible operations: she can either cut the top of a
tree, decreasing its height by one (at cost of 1) or cut the tree
down (at cost of height i).

Input
The first line of input will contain 1 ≤ N ≤ 3*105, the number of trees.

The next line will contain N integers 0 ≤ Hi ≤ 109

Output
Print the minimal cost to make the height of all trees in alley equal.


Example Input
5
1 2 3 4 5
Example Output
6
"""
# INT_MAX = (1 << 31) - 1
import sys
INT_MAX = sys.maxsize


def minimal_cost_to_make_alley(height_arr, N):
    # sort in decreasing
    height_arr.sort(reverse=True)

    # Take suffix sum from end of array
    suffix_sum = [0] * (N + 1)
    suffix_sum[N-2] = height_arr[N-2]

    for i in range(N-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + height_arr[i]
    # print("suffix_sum: ", suffix_sum)

    # take diff from max height tree to current tree
    prefix_diff = [0] * N
    # initalize with 0
    prefix_diff[0] = 0
    for i in range(1, N):
        # to convert high height to current height take diff * No of tree
        # (index) + previous diff
        prefix_diff[i] = prefix_diff[i-1] + ((
                    height_arr[i-1] - height_arr[i]) * i)
    # print("prefix_diff: ", prefix_diff)

    # final loop to calculate minimal cost to make height
    # All trees on right should be cut and all trees on left should be removed!

    # suffix_sum is cost to cut right side trees
    # prefix_diff is cost to remove height of each tree

    ans = INT_MAX
    for i in range(0, N):
        ans = min(ans, (prefix_diff[i] + suffix_sum[i+1]))

    return ans


if __name__ == '__main__':
    N = int(input())
    height_arr = list(map(int, input().split()))
    print(minimal_cost_to_make_alley(height_arr, N))
