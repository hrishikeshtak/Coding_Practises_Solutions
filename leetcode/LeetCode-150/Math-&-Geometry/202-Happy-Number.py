"""
202. Happy Number
"""


class Solution:
    def isHappy(self, N: int) -> bool:
        numbers = set()
        while True:
            square_sum = 0
            while N:
                square_sum += ((N % 10) * (N % 10))
                N = N // 10
            N = square_sum
            # print(f"square_sum: {square_sum}")
            # print(f"numbers: {numbers}")
            if N == 1:
                return True
            if N in numbers:
                return False
            numbers.add(N)
