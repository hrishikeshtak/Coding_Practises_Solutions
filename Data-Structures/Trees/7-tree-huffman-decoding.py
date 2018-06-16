#!/usr/bin/python

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    # Enter Your Code Here
    result = list()
    current = root
    for bit in s:
        if '0' == bit:
            current = current.left
        elif '1' == bit:
            current = current.right
        if current.left is None and current.right is None:
            result.append(current.data)
            current = root
    print "".join(result)
