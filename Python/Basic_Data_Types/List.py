#!/usr/bin/env python3

# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Sample Input

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())
    lst = []
    try:
        for i in range(N):
            line = input()
            func_name = line.split()[0]
            if func_name == 'insert':
                position = int(line.split()[1])
                element = int(line.split()[2])
                lst.insert(position, element)
            elif func_name == 'print':
                print(lst)
            elif func_name == 'remove':
                element = int(line.split()[1])
                lst.remove(element)
            elif func_name == 'append':
                element = int(line.split()[1])
                lst.append(element)
            elif func_name == 'sort':
                lst.sort()
            elif func_name == 'pop':
                lst.pop()
            elif func_name == 'reverse':
                lst.reverse()
    except Exception as err:
        print(err)
