"""
295. Find Median from Data Stream
"""

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n % 2 != 0:
            return self.arr[n // 2]
        else:
            return (self.arr[n//2] + self.arr[(n//2)-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(f"findMedian of arr: {obj.arr} is {obj.findMedian()}")
obj.addNum(3)
print(f"findMedian of arr: {obj.arr} is {obj.findMedian()}")
