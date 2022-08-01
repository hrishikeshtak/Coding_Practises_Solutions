"""
125. Valid Palindrome

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphanum(s[l]):
                l += 1
            while l < r and not self.isAlphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

    def isAlphanum(self, char: str) -> bool:
        return ord('A') <= ord(char) <= ord('Z') or \
               ord('a') <= ord(char) <= ord('z') or \
               ord('0') <= ord(char) <= ord('9')

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
