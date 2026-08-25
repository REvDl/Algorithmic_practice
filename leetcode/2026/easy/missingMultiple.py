from typing import List



class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = k
        nums_set = set(nums)
        while True:
            if multiple not in nums_set:
                return multiple
            multiple += k





obj = Solution()
nums = [8,2,3,4,6]
k = 2
print(obj.missingMultiple(nums, k))
