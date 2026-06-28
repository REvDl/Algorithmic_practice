from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                grow = all(nums[i] > nums[i - 1] for i in range(1, p+1))
                fall = all(nums[i] < nums[i - 1] for i in range(p+1, q+1))
                grow_2 = all(nums[i] > nums[i - 1] for i in range(q+1, n))
                if grow and fall and grow_2:
                    return True
        return False
