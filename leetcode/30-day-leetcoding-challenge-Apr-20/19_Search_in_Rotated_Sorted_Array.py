#!/usr/bin/python3

"""
Search in Rotated Sorted Array
"""


class Solution:
    def search(self, arr: 'List[int]', target: int) -> int:

        lo = 0
        hi = len(arr) - 1

        pivot = self.findPivot(arr, lo, hi)

        if pivot == -1:
            return -1

        if arr[pivot] == target:
            return pivot

        if target >= arr[lo]:
            return self.binarySearch(arr, lo, pivot, target)
        return self.binarySearch(arr, pivot+1, hi, target)

    def binarySearch(self, arr, lo, hi, key):

        if hi < lo:
            return -1
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid

        if key >= arr[mid]:
            return self.binarySearch(arr, mid+1, hi, key)
        return self.binarySearch(arr, lo, mid-1, key)

    def findPivot(self, arr, lo, hi):
        if hi < lo:
            return -1
        if lo == hi:
            return lo

        mid = (lo + hi) // 2

        if mid < hi and arr[mid] > arr[mid+1]:
            return mid
        if mid > lo and arr[mid] < arr[mid-1]:
            return mid-1

        if arr[mid] >= arr[lo]:
            return self.findPivot(arr, mid+1, hi)
        return self.findPivot(arr, lo, mid-1)



if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(f"{Solution().search(arr, 5)}")
