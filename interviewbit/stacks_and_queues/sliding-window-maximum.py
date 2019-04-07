#!/usr/bin/python3

from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, arr, K):
        res = []
        N = len(arr)
        if K > N:
            res.append(max(arr))
            return

        dq = deque()
        for i in range(K):
            # print(dq)
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            dq.append(i)

        for i in range(K, N):
            # print(dq)
            res.append(arr[dq[0]])
            # print(res)
            while dq and dq[0] <= i-K:
                # print(arr[i], arr[i-K])
                dq.popleft()
            # print(dq)

            while dq and arr[i] >= arr[dq[-1]]:
                # print(arr[i], dq[-1])
                dq.pop()
            # print(dq)
            dq.append(i)
            # print(dq)
        res.append(arr[dq[0]])
        return res


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(Solution().slidingMaximum(arr, K))
