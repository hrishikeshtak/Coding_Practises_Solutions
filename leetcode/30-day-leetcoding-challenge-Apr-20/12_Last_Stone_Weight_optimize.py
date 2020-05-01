#!/usr/bin/python3

"""
Last Stone Weight
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of
weight y has new weight y-x.
At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""

import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        stones = list(map(lambda x: -x, stones))

        # heapify list
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, -abs(x - y))

        return 0 if not stones else -stones[0]


if __name__ == '__main__':
    A = [2, 7, 4, 1, 8, 1]
    # A = [2, 2, 3, 4]
    print(f"lastStoneWeight: {Solution().lastStoneWeight(A)}")
