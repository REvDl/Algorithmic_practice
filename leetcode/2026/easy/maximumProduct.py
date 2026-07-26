from typing import List



class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res_one = nums[-1] * nums[-2] * nums[-3]
        res_two = nums[0] * nums[1] * nums[-1]
        return max(res_one, res_two)



obj = Solution()
nums = [-100,-98,-1,2,3,4]
print(obj.maximumProduct(nums))
