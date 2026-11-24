from typing import List
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = float('-inf')
        n = len(nums)
        for i in range(n):
            zeros = 0
            p, g, l = 1, 0, 1
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros > 0:
                    continue
                x = nums[j]
                p *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)
                if p == (g * l):
                    res = max(res, j - i + 1)
        return res



obj = Solution()
nums = [1,2,1,2,1,1,1]
print(obj.maxLength(nums))
