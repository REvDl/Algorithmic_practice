from typing import List
from functools import cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]
        @cache
        def get_sum(i: int, j: int):
            if i == j:
                return 0
            ans = 0
            for k in range(i, j):
                left = prefix_sum[k + 1] - prefix_sum[i]
                right = prefix_sum[j + 1] - prefix_sum[k + 1]
                if left < right:
                    take = left + get_sum(i, k)
                elif left > right:
                    take = right + get_sum(k + 1, j)
                else:
                    take = right + max(get_sum(i, k), get_sum(k + 1, j))
                ans = max(ans, take)
            return ans
        get_sum.cache_clear()
        return get_sum(0, n - 1)



obj = Solution()
stoneValue = [6,2,3,4,5,5]
print(obj.stoneGameV(stoneValue))
