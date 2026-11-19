from typing import List



class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(abs(nums[2] - nums[-1]), abs(nums[0] - nums[-3]), abs(nums[1] - nums[-2]))



obj = Solution()
nums = [[1,4,7,8,5], [1,4,3]]
for num in nums:
    print(obj.minimizeSum(num))

