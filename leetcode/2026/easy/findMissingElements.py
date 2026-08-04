from typing import List



class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        res = []
        for num in range(min(nums), max(nums)):
            if num not in nums_set:
                res.append(num)
        return res



obj = Solution()
nums = [1,4,2,5]
print(obj.findMissingElements(nums))
