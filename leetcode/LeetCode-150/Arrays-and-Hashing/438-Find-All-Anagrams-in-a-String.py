"""
438. Find All Anagrams in a String
"""

from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        ans = []
        if m > n:
            return ans
        p_dict = defaultdict(int)
        for i in range(m):
            p_dict[p[i]] += 1
        
        def isAnagram(temp_dict):
            for i in p_dict:
                if p_dict[i] != temp_dict[i]:
                    return False
            return True

        i = 0
        j = 0
        temp_dict = defaultdict(int)
        while j < m:
            temp_dict[s[j]] += 1
            j += 1
        
        while i <= (n-m):
            if isAnagram(temp_dict):
                ans.append(i)
            # print(i, j, ans, temp_dict)
            if j >= n:
                break
            # decrease counter for i
            temp_dict[s[i]] -= 1
            temp_dict[s[j]] += 1
            i += 1
            j += 1
            
        return ans
