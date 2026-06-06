from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array_sum = sum(nums)
        left_sum = 0
        ans = []
        for i in range(n):
            right_sum = array_sum - left_sum - nums[i]
            ans.append(abs(right_sum - left_sum))
            left_sum += nums[i]
        return ans



obj = Solution()
nums = [10, 4, 8, 3]
print(obj.leftRightDifference(nums))
