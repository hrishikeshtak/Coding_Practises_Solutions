#!/usr/bin/python3

import heapq
M = int(1e9+7)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, K, arr):
        # print(arr)
        arr = list(map(lambda x: -x, arr))
        heapq.heapify(arr)
        # print(arr)
        ans = 0
        for _ in range(K):
            # print(arr)
            temp = -heapq.heappop(arr)
            ans = (ans + temp) % M
            heapq.heappush(arr, -(temp//2))
        return ans % M


if __name__ == '__main__':
    K = 3
    A = [6, 5]
    K = 10
    A = [2147483647, 2000000014, 2147483647 ]
    print(Solution().nchoc(K, A))
