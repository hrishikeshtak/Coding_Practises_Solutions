"""
191. Number of 1 Bits

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt


n = 1011
print(Solution().hammingWeight(int(n)))
