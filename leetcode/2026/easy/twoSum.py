from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        target_copy = target
        for i, num in enumerate(nums):
            target_copy = target - num
            if target_copy in hash_map:
                return [i, hash_map[target_copy]]
            else:
                hash_map[num] = i




obj = Solution()
nums = [3,2,4]
target = 6
print(obj.twoSum(nums,target))
