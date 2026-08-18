from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      need_sum = 0
      for num in range(n+1):
        need_sum += num
      return need_sum - sum(nums)

  
    def missingNumber_short(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)



obj = Solution()
nums = [0, 1]
print(obj.missingNumber(nums))