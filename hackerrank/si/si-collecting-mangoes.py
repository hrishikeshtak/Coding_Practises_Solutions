#!/usr/bin/python3


def collecting_mangoes(operations, N):
    # print("operations: ", operations)
    stack = [0] * (N+1)
    max_stack = [0] * (N+1)
    max_top = -1
    top = -1

    for i in range(0, N):
        # print(operations[i])
        # Push
        if len(operations[i]) == 2:
            top += 1
            stack[top] = int(operations[i][1])
            if stack[top] >= max_stack[max_top]:
                max_top += 1
                max_stack[max_top] = stack[top]
            # print("stack: ", stack)
            # print("max_stack: ", max_stack)
        # Display Max
        elif operations[i][0] == 'Q':
            if max_top == -1:
                print("Empty")
            else:
                print(max_stack[max_top])
        # Pop
        else:
            if top <= -1 or max_top <= -1:
                continue
            if stack[top] == max_stack[max_top]:
                top -= 1
                max_top -= 1
            else:
                top -= 1


if __name__ == '__main__':
    for i in range(int(input())):
        N = int(input())
        operations = []
        for _ in range(N):
            operations.append(input().split(" ", 1))
        print("Case {}:".format(i+1))
        collecting_mangoes(operations, N)
