"""
20. Valid Parentheses
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        HashMap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c not in HashMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != HashMap[c]:
                return False
            stack.pop()
        return not stack
