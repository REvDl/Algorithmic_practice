from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0 for _ in range(10**5+1)]
        max_ice = 0
        for price in costs:
            count[price] += 1
        for price in range(len(count)):
            if count[price] > 0:
                can_buy = coins // price
                really_buy = min(can_buy, count[price])
                if price <= coins:
                    coins -= really_buy * price
                    max_ice += really_buy
                else:
                    break
        return max_ice



obj = Solution()
costs = [1,3,2,4,1]
coins = 7
print(obj.maxIceCream(costs, coins))
