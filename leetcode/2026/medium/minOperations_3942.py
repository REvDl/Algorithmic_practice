from typing import List


class Solution:
    def canSorting(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                count += 1
        if nums[n - 1] > nums[0]:
            count += 1
        return count <= 1



    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if not self.canSorting(nums) and not self.canSorting(nums[::-1]):
            return -1
        res = []
        idx = nums.index(0)
        if self.canSorting(nums):
            res.append(idx)
            res.append(n - idx + 2)
        if self.canSorting(nums[::-1]):
            idx = nums[::-1].index(0)
            res.append(n - idx)
            res.append(idx + 2)
        return min(res)


obj = Solution()
nums = [0, 2, 1]
print(obj.minOperations(nums))
