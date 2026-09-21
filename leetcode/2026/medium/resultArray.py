from typing import List
import math
from collections import Counter


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arrays = []
        for i in range(n):
            for j in range(i, n):
                arrays.append(math.prod(nums[i:j+1]) % k)
        count = Counter(arrays)
        res = []
        for i in range(0, k):
            res.append(count[i])
        return res

obj = Solution()
nums = [1,2,3,4,5]
k = 3
print(obj.resultArray(nums, k))
