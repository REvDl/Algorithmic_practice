


class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        items = [(need1, cost1), (need2, cost2)]
        (min_need, min_cost), (max_need, max_cost) = sorted(items)
        ans1 = cost1 * need1 + cost2 * need2
        ans2 = costBoth * max_need
        ans3 = (costBoth * min_need) + ((max_need - min_need) * max_cost)
        return min(ans1, ans2, ans3)




obj = Solution()
cost1 = 3
cost2 = 2
costBoth = 1
need1 = 3
need2 = 2
print(obj.minimumCost(cost1, cost2, costBoth, need1, need2))
