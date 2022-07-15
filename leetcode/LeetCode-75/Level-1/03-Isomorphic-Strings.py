"""
Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
"""

from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_isomorphic_dict: Dict[str, str] = {}
        t_isomorphic_dict: Dict[str, str] = {}

        for i in range(0, len(s)):
            if s[i] not in s_isomorphic_dict and t[i] not in t_isomorphic_dict:
                # if both char from s and t string not present in hashmap
                s_isomorphic_dict[s[i]] = t[i]
                t_isomorphic_dict[t[i]] = s[i]
            elif s_isomorphic_dict.get(s[i]) != t[i] or t_isomorphic_dict.get(t[i]) != s[i]:
                return False
            # elif s[i] not in s_isomorphic_dict and t[i] in t_isomorphic_dict:
            #     if t_isomorphic_dict[t[i]] != s[i]:
            #         return False
            # elif s[i] in s_isomorphic_dict and t[i] in t_isomorphic_dict:
            #     if s_isomorphic_dict[s[i]] != t[i]:
            #         return False
            # elif s[i] in s_isomorphic_dict and t[i] not in t_isomorphic_dict:
            #     if s_isomorphic_dict[s[i]] != t[i]:
            #         return False

            # print(f"s_isomorphic_dict: {s_isomorphic_dict}")
            # print(f"t_isomorphic_dict: {t_isomorphic_dict}")
        return True


if __name__ == '__main__':
    str1 = "egg"
    str2 = "add"

    str1 = "foo"
    str2 = "bar"

    str1 = "paper"
    str2 = "title"

    str1 = "badc"
    str2 = "baba"

    print(f"str1: {str1} str2: {str2}")

    print(Solution().isIsomorphic(str1, str2))
