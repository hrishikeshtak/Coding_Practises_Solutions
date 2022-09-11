"""
76. Minimum Window Substring
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, countS = {}, {}
        res, reslen = [-1, -1], float("infinity")
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)
            if c in countT and countS[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""