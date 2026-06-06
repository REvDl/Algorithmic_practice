from typing import List





class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        leftSum, rightSum = 0, 0
        for i, num in enumerate(nums):
            if leftSum == (total_sum - leftSum - num):
                return i
            leftSum += num
        return -1


obj = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(obj.pivotIndex(nums))
