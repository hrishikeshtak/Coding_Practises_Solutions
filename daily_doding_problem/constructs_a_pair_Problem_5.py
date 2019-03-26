#!/usr/bin/python3

"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def func(a, b):
    return a


def func1(a, b):
    return b


def car(somefunction):
    # print(somefunction)
    return somefunction(func)


def cdr(somefunction):
    # print(somefunction)
    return somefunction(func1)


# a = cons(3, 4)
# print(a(func))
# print(a(func1))

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
