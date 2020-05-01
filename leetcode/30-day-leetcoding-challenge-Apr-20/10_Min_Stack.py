#!/usr/bin/python3

"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif x <= self.min_stack_top():
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.top() == self.min_stack[-1]:
            _ = self.min_stack.pop()
        _ = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min_stack_top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(-2)
    # obj.push(0)
    # obj.push(-3)
    # print(f"getMin: {obj.getMin()}")
    # obj.pop()
    # print(f"top: {obj.top()}")
    # print(f"getMin: {obj.getMin()}")

    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(f"getMin: {obj.getMin()}")
    obj.pop()
    print(f"getMin: {obj.getMin()}")
