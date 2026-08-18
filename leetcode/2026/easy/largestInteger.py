from audioop import maxpp
from typing import List
from collections import Counter, defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
      n = len(nums)
      count = Counter(nums)
      max_elements = []
      if k == n:
        return max(nums)
      elif k == 1:
        for num in nums:
          if count[num] == 1:
            max_elements.append(num)
      else:
        left, right = nums[0],nums[-1]
        
        if count[left] == 1:
          max_elements.append(left)
        if count[right] == 1:
          max_elements.append(right)
      return -1 if not max_elements else max(max_elements)



obj = Solution()
nums = [3,9,2,1,7]
k = 3
print(obj.largestInteger(nums, k))