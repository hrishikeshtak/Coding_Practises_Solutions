#!/usr/bin/python3

from itertools import accumulate
from collections import Counter


n1, n2, n3 = map(int, input().split())
# store seq in reverse order
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))
seq3 = list(map(int, input().split()))

# print(seq1, seq2, seq3)

seq1 = list(accumulate(seq1[::-1]))
seq2 = list(accumulate(seq2[::-1]))
seq3 = list(accumulate(seq3[::-1]))
# print(seq1, seq2, seq3)

total_stack = seq1 + seq2 + seq3
Counter_stack = Counter(total_stack)
# Counter is used to check presence of number 3 times in stack
# that means height is matched with other arrays
try:
    print(max(i[0] for i in Counter_stack.items() if i[1] == 3))
except Exception:
    print(0)
