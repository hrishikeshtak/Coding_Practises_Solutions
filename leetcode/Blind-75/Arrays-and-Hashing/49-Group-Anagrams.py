"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            hashmap["".join(sorted(i))].append(i)
        return hashmap.values()



if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"groupAnagrams: {Solution().groupAnagrams(strs)}")
