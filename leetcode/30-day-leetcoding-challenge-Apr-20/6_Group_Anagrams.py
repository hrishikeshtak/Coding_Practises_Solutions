#!/usr/bin/python3

"""
Group Anagrams
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

from collections import defaultdict


class Solution(object):
    """Group Anagrams"""
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            group_anagrams[sorted_word].append(word)

        result = []
        for anagram in group_anagrams:
            result.append(group_anagrams[anagram])

        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"output: {Solution().groupAnagrams(strs)}")
