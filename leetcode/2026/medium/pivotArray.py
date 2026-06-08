from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        big_pivot, small_pivot, mid_pivot = [], [], []
        for num in nums:
            if num > pivot:
                big_pivot.append(num)
            elif num == pivot:
                mid_pivot.append(num)
            else:
                small_pivot.append(num)
        return small_pivot + mid_pivot + big_pivot
