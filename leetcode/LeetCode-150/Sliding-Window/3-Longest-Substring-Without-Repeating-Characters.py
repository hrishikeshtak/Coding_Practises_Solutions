"""
3. Longest Substring Without Repeating Characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        n = len(s)
        i = 0
        res = 0
        for j in range(len(s)):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            visited.add(s[j])
            res = max(res, (j - i + 1))
        return res
