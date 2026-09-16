import math


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % (10**9 + 7)



obj = Solution()
n, k = 4, 2
print(obj.numberOfSets(n,k))
