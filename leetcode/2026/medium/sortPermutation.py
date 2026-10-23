from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        indexes = [nums[i] for i in range(n) if nums[i] != i]
        res = indexes[0] if indexes else 0
        for x in indexes[1:]:
            res &= x
        return res



# 0 3 2 1
# 

obj = Solution()
nums =[0,2,3,1]
print(obj.sortPermutation(nums))
