from typing import List
import bisect
import math
from itertools import combinations



class Solution:
    def _count_x(self, x: int, coins):
        total = 0
        n = len(coins)
        for size in range(1, n + 1):
            for group in combinations(coins, size):
                curr_lcm = math.lcm(*group)
                count = x // curr_lcm
                if size % 2 == 1:
                    total += count
                else:
                    total -= count
        return total


    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        left, right = 1, min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if self._count_x(mid, coins) < k:
                left = mid + 1
            else:
                right = mid
        return right



obj = Solution()
coins = [3,6,9]
k = 3
print(obj.findKthSmallest(coins, k))
