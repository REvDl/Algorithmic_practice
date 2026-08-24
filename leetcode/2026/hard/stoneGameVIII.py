from typing import List



class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        max_prefix = prefix_sum[n]
        for i in range(n-1, 1, -1):
            max_prefix = max(max_prefix, prefix_sum[i] - max_prefix)
        return max_prefix


obj = Solution()
stones = [-1,2,-3,4,-5]
print(obj.stoneGameVIII(stones))
