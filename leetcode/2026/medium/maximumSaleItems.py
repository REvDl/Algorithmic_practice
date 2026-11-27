from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus  = [0 for _ in range(n)]
        for i in range(n):
            curr = 1
            for j in range(n):
                factor_i, factor_j = items[i][0], items[j][0]
                if i != j:
                    if factor_j % factor_i == 0:
                        curr += 1
                bonus[i] = curr
        dp = [0 for _ in range(budget + 1)]
        for i in range(n):
            _, price = items[i]
            for b in range(budget, price - 1, - 1):
                dp[b] = max(dp[b], dp[b - price] + bonus[i])
            for b in range(price, budget + 1):
                dp[b] = max(dp[b], dp[b - price] + 1)
        return max(dp)




obj = Solution()
items = [[6,2],[2,6],[3,4]]
budget = 9
print(obj.maximumSaleItems(items, budget))


