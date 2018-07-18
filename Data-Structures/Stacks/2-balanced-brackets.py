#!/bin/python3

balanced_dict = {')': '(', ']': '[', '}': '{'}


def isBalanced(s):
    stack = list()
    for c in s:
        if stack and balanced_dict.get(c) == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "NO" if stack else "YES"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
