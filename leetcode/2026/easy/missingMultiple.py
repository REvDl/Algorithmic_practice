from typing import List



class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = 1
        while True:
            if multiple not in nums and multiple % k == 0:
                return multiple
            multiple += 1





obj = Solution()
nums = [8,2,3,4,6]
k = 2
print(obj.missingMultiple(nums, k))
