#!/usr/bin/python3

# p1 = Find 1st smaller elements on left side
# p2 = Find 1st smaller elements on right side
# area = arr(i) * (p2 - p1 - 1)
# Time Complexity: Since every bar is pushed and popped only once,
# the time complexity of this method is O(n).
INT_MIN = -(1 << 31)


def first_smaller_on_left(arr, N):
    s = [-1] * N
    b = [-1] * N
    top = -1
    top += 1
    s[top] = 0

    for i in range(1, N):
        # print("stack: ", s)
        # print("b: ", b)
        while top >= 0:
            if arr[i] > arr[s[top]]:
                b[i] = s[top]
                top += 1
                s[top] = i
                break
            else:
                top -= 1
        if top == -1:
            b[i] = -1
            top += 1
            s[top] = i
    return b


def first_smaller_on_right(arr, N):
    s = [-1] * N
    b = [N] * N
    top = -1
    top += 1
    s[top] = N-1

    for i in range(N-2, -1, -1):
        # print("stack: ", s)
        # print("b: ", b)
        while top >= 0:
            if arr[i] > arr[s[top]]:
                b[i] = s[top]
                top += 1
                s[top] = i
                break
            else:
                top -= 1
        if top == -1:
            b[i] = N
            top += 1
            s[top] = i
    # print(b)
    return b


def rect_area(arr, N):
    left_arr = first_smaller_on_left(arr, N)
    right_arr = first_smaller_on_right(arr, N)
    # print("left_arr: ", left_arr)
    # print("right_arr: ", right_arr)
    ans = INT_MIN
    for i in range(0, N):
        p1 = left_arr[i]
        p2 = right_arr[i]
        area = ((p2 - p1 - 1) * arr[i])
        ans = max(ans, area)
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(rect_area(arr, N))
