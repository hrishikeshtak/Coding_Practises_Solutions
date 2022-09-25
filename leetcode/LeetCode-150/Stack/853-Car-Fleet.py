"""
853. Car Fleet
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        temp = [(p, s) for p, s in zip(position, speed)]
        temp.sort()  # sort based on cars position
        for p, s in temp[::-1]:
            rem_dis = (target - p) / s
            if stack and stack[-1] >= rem_dis:
                pass
            else:
                stack.append(rem_dis)
        return len(stack)
