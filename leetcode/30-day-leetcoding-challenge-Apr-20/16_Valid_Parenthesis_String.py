#!/usr/bin/python3

"""
Valid Parenthesis String

Given a string containing only three types of characters:
'(', ')' and '*', write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.
An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True

        if s[0] == ')' or s[-1] == '(':
            return False

        low = 0
        high = 0

        for i in range(0, len(s)):
            if s[i] == '(':
                low += 1
                high += 1
            elif s[i] == ')':
                if low > 0:
                    low -= 1
                high -= 1
                if high < 0:
                    return False
            else:
                if low > 0:
                    low -= 1
                    high += 1

        return low == 0


if __name__ == '__main__':
    s = "()"
    print(f"{Solution().checkValidString(s)}")
    s = "(*)"
    print(f"{Solution().checkValidString(s)}")
    s = "(*))())"
    print(f"{Solution().checkValidString(s)}")
    s = "((*)**)(*))))))"
    print(f"{Solution().checkValidString(s)}")
    s = ""
    print(f"{Solution().checkValidString(s)}")
    s = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
    print(f"{Solution().checkValidString(s)}")
    s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    print(f"{Solution().checkValidString(s)}")
