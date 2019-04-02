#!/usr/bin/python3

# Optimal: Find first max on left side


def stock_pain(arr, N):
    # print(arr)
    stack = [0] * (N)
    result = [0] * (N)
    top = -1
    top += 1
    stack[top] = 0
    # first element, only this element is max on left side
    result[top] = 1
    for i in range(1, N):
        while top >= 0:
            if arr[i] < arr[stack[top]]:
                result[i] = stack[top]
                # print(i - stack[top], end=" ")
                top += 1
                stack[top] = i
                break
            else:
                top -= 1
        if top == -1:
            # no other element is max on left side
            result[i] = top
            # print(1, end=" ")
            top += 1
            stack[top] = i
    # print(result)
    print(result[0], end=" ")
    for i in range(1, N):
        print(i - result[i], end=" ")


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        stock_pain(arr, N)
        print()
