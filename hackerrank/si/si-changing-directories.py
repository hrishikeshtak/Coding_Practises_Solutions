#!/usr/bin/python3

stack = [0] * 300
top = -1


def change_directory(operation):
    global stack, top
    if operation[0] == "cd" and operation[1] == "/":
        top = -1
    elif operation[0] == "cd":
        if operation[1][0] == "/":
            top = -1
        cmd = operation[1].split("/")
        for i in cmd:
            if i == "":
                continue
            elif i == ".." and top == -1:
                continue
            elif i == "..":
                top -= 1
            else:
                top += 1
                stack[top] = i
            # print(stack)
    elif operation[0] == "pwd":
        # print("top: ", top)
        if top == -1:
            print("/")
        else:
            for i in range(0, top+1):
                print("/{}".format(stack[i]), end="")
            print("/")


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        for _ in range(N):
            operation = input().split(" ", 1)
            change_directory(operation)
        print()
