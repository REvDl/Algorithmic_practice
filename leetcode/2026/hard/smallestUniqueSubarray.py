from typing import List
from collections import defaultdict



class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        b = 10 ** 5 + 1
        def has_unique(l: int) -> bool:
            max_pow = pow(b, l - 1, mod)
            counts = defaultdict(int)
            h = 0
            for i in range(l):
                h = (h * b + nums[i]) % mod
            counts[h] += 1
            for right in range(l, n):
                h = (h - nums[right - l] * max_pow) % mod
                h = (h * b + nums[right]) % mod
                counts[h] += 1
            return 1 in counts.values()

        left_l, right_l = 1, n
        ans = n
        while left_l <= right_l:
            mid = (left_l + right_l) // 2
            if has_unique(mid):
                ans = mid
                right_l = mid - 1
            else:
                left_l = mid + 1
        return ans

obj = Solution()
nums = [3,3,3]
print(obj.smallestUniqueSubarray(nums))
