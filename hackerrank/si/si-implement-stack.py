#!/usr/bin/python3
s = [0] * 10000
top = -1


def stack(operation):
    global s
    global top
    # print(s)
    # print(operation)
    # print("top: ", top)
    if operation[0].lower() == "push":
        x = int(operation[1])
        # print(x)
        top += 1
        s[top] = x
    elif operation[0].lower() == "pop":
        if top == -1:
            print("Empty")
        else:
            print(s[top])
            top -= 1


if __name__ == '__main__':
    for _ in range(int(input())):
        operation = input().split(" ", 1)
        stack(operation)
