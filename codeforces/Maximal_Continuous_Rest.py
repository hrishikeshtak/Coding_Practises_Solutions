#!/usr/bin/python3


def max_contiguous_ones(arr, N):
    # print(arr)
    temp = 0
    if arr[0] == arr[-1] == 1:
        temp += 1

    # print("t: ", temp)
    count = 0
    ans = 0
    for i in range(0, N):
        # print("count: ", count)
        if arr[i] == 1:
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    if ans == 1:
        return ans + temp
    else:
        return ans


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_contiguous_ones(arr, N))
