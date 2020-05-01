#!/usr/bin/python3

"""
Backspace String Compare

Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace character.

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        i = len(S) - 1
        j = len(T) - 1

        s_backspace_count = 0
        t_backspace_count = 0

        if S[i] != T[j]:
            return False

        while i >= 0 or j >= 0:
            while i >= 0 and (s_backspace_count > 0 or S[i] == '#'):
                if S[i] == '#':
                    s_backspace_count += 1
                else:
                    s_backspace_count -= 1
                i -= 1

            while j >= 0 and (t_backspace_count > 0 or T[j] == '#'):
                if T[j] == '#':
                    t_backspace_count += 1
                else:
                    t_backspace_count -= 1
                j -= 1

            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
            else:
                if i >= 0 or j >= 0:
                    return False

        return i < 0 and j < 0


if __name__ == '__main__':
    S = 'ab#c'
    T = 'ad#c'

    print(f"{Solution().backspaceCompare(S, T)}")

    S = 'ab##'
    T = 'c#d#'

    print(f"{Solution().backspaceCompare(S, T)}")

    S = 'ab##'
    T = 'c#'

    print(f"{Solution().backspaceCompare(S, T)}")

    S = "y#fo##f"
    T = "y#f#o##f"

    print(f"{Solution().backspaceCompare(S, T)}")
