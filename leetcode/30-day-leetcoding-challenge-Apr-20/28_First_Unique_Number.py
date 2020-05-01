#!/usr/bin/python3

"""
First Unique Number

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
"""

from collections import deque, defaultdict


class FirstUnique:

    def __init__(self, nums: 'List[int]'):
        self.nums = deque()
        self.map = defaultdict(lambda: 0)
        for i in nums:
            self.map[i] += 1
            self.nums.append(i)

    def showFirstUnique(self) -> int:
        # import pdb; pdb.set_trace()
        while self.nums and self.map[self.nums[0]] > 1:
            self.nums.popleft()

        if not self.nums:
            return -1
        return self.nums[0]

    def add(self, value: int) -> None:
        self.map[value] += 1
        if self.map[value] == 1:
            self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# firstunique = FirstUnique([2, 3, 5])
# print(firstunique.showFirstUnique())
# firstunique.add(5)
# print(firstunique.showFirstUnique())
# firstunique.add(2)
# print(firstunique.showFirstUnique())
# firstunique.add(3)
# print(firstunique.showFirstUnique())


firstunique = FirstUnique([7, 7, 7, 7, 7, 7])
print(firstunique.showFirstUnique())
firstunique.add(7)
firstunique.add(3)
firstunique.add(3)
firstunique.add(7)
firstunique.add(17)
print(firstunique.showFirstUnique())

firstunique = FirstUnique([809])
print(firstunique.showFirstUnique())
firstunique.add(809)
print(firstunique.showFirstUnique())
