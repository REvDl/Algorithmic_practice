from typing import List





class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        max_prefix_sum = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                max_prefix_sum += nums[i]
            else:
                break
        nums_set = set(nums)
        while max_prefix_sum in nums_set:
            max_prefix_sum += 1
        return max_prefix_sum

obj = Solution()
nums = [38]
res = obj.missingInteger(nums)
print(res)
assert res == 6
