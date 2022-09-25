"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     N = len(nums1)
    #     M = len(nums2)

    #     if N == 0 and M != 0:
    #         return nums2[M//2]
    #     elif M == 0 and N != 0:
    #         return nums1[N//2]
        
    #     K = (N + M) // 2
    #     if (N + M) % 2 != 0:  # odd length
    #         m1 = self.median(nums1, nums2, N, M, K)
    #         return m1
    #     else:  # even length
    #         m1 = self.median(nums1, nums2, N, M, K)
    #         m2 = self.median(nums1, nums2, N, M, K-1)
            
    #         return (m1 + m2) / 2
    
    # def median(self, num1, num2, N, M, K):
    #     lo = min(num1[0], num2[0])
    #     hi = max(num1[-1], num2[-1])
        
    #     ans = -1
        
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         # get the elements less than mid from num1 and num2
    #         num1_less = self.floor(num1, mid)
    #         num2_less = self.floor(num2, mid)
    #         # add 1 as index starts from 0
    #         less = num1_less + num2_less + 1
    #         if less == K:
    #             # check if element present in one of the array, if present return element
    #             if self.binary_search(num1, mid) or self.binary_search(num2, mid):
    #                 return mid
    #             else:
    #                 lo = mid + 1
    #         elif less <= K:
    #             lo = mid + 1
    #         else:
    #             hi = mid - 1
    #     return ans
                
    
    # def binary_search(self, arr, k):
    #     lo, hi = 0, len(arr) -1
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if arr[mid] == k:
    #             return True
    #         if arr[mid] <= k:
    #             lo = mid + 1
    #         else:
    #             hi = mid - 1
    #     return False
                
    
    # def floor(self, arr, k):
    #     # return index of element <= k
    #     lo, hi = 0, len(arr) - 1
    #     ans = 0
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if arr[mid] < k:
    #             ans = mid
    #             lo = mid + 1
    #         else:
    #             hi = mid - 1
    #     return ans

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
            # make A as a smaller array to apply BS
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A Pointer
            j = half - i - 2 # B Pointer, sub 2 as indexes starts from 0
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")
            
            # find if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    # odd length
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # more elements from A
                r = i - 1
            else:
                l = i + 1
                
        




nums1 = [1, 3]
nums2 = [2]
nums1 = [0, 0]
nums2 = [0, 0]
print(f"nums1: {nums1} nums2: {nums2}")
print(f"findMedianSortedArrays: {Solution().findMedianSortedArrays(nums1, nums2)}")
