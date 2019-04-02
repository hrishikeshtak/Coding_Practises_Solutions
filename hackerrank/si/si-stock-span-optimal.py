#!/usr/bin/python3

# Brute Force


def stock_pain(arr, N):
    stack = [0] * (N+1)
    top = -1
    for i in range(0, N):
        top += 1
        stack[top] = arr[i]
        k = top
        cnt = 0
        # print(stack, k)
        while k >= 0:
            if arr[i] >= stack[k]:
                cnt += 1
            else:
                break
            k -= 1
        print(cnt, end=" ")


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        stock_pain(arr, N)
        print()
