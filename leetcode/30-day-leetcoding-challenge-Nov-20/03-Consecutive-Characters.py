#!/usr/bin/python3

"""
Consecutive Characters
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Input: s = "hooraaaaaaaaaaay"
Output: 11
"""


class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i+1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
                
        return ans
