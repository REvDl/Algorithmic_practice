from typing import List



class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            num = nums[i]
            if num > 0:
                circle_idx = (i + num) % n
                result[i] = nums[circle_idx]
            elif num < 0:
                circle_idx = (i - abs(num)) % n
                result[i] = nums[circle_idx]
            else:
                result[i] = 0
        return result


obj = Solution()
nums = [-1,4,-1]
print(obj.constructTransformedArray(nums))
