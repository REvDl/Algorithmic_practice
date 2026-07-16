from math import gcd
from itertools import accumulate

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        mx = list(accumulate(nums, max))
        prefixGcd = [gcd(mx[i], nums[i]) for i in range(n)]
        prefixGcd.sort()
        left, right = 0, n - 1
        res = 0
        while left < right:
            res += gcd(prefixGcd[left], prefixGcd[right]) 
            left += 1
            right -= 1
        return res


obj = Solution()
nums = [2,6,4]
print(obj.gcdSum(nums))

