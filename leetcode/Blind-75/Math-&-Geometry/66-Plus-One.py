"""
66. Plus One
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst_to_str = "".join(str(i) for i in digits)
        # print(lst_to_str)
        new_number = int(lst_to_str) + 1
        return [int(i) for i in str(new_number)]