#!/usr/bin/python3

"""
Perform String Shifts
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
"""


class Solution:
    def stringShift(self, s: str, shift: 'List[List[int]]') -> str:
        """
        Hint: You may notice that left shift cancels the right shift
        so count the total left shift times (may be negative if the
        final result is right shift), and perform it once.
        """
        # count left shift amount and right count amount
        count_left_shift = 0
        count_right_shift = 0

        for i in shift:
            if i[0] == 0:
                count_left_shift += i[1]
            else:
                count_right_shift += i[1]

        if count_left_shift == count_right_shift:
            return s

        if count_left_shift < count_right_shift:
            count_right_shift = count_right_shift - count_left_shift
            count_left_shift = 0
        else:
            count_left_shift = count_left_shift - count_right_shift
            count_right_shift = 0

        if count_left_shift > 0:
            # left shift
            count_left_shift = count_left_shift % len(s)
            return s[count_left_shift:] + s[:count_left_shift]
        else:
            # right shift
            count_right_shift = count_right_shift % len(s)
            return s[-count_right_shift:] + s[:-count_right_shift]


if __name__ == '__main__':
    s = "abc"
    shift = [[0, 1], [1, 2]]
    print(f"{Solution().stringShift(s, shift)}")
    s = "abcdefg"
    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    print(f"{Solution().stringShift(s, shift)}")
    s = "xqgwkiqpif"
    shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    print(f"{Solution().stringShift(s, shift)}")
