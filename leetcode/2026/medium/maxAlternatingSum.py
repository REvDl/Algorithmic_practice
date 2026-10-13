from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        n = len(nums)
        res = 0
        for i in range(n):
            if i % 2 == 0:
                index = -1 - (i // 2)
            else:
                index = i // 2
            current_element = nums[index]
            if i % 2 == 0:
                res += (current_element) ** 2
            else:
                res -= (current_element) ** 2
        return res





obj = Solution()
nums = [1,2,3]
print(obj.maxAlternatingSum(nums))
