from typing import List



class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return True if count <= 1 else False               





obj = Solution()
nums = [3,4,5,1,2]
print(obj.check(nums))
