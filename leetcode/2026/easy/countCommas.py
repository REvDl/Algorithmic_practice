

class Solution:
    def countCommas_v1(self, n: int) -> int:
        if n < 1000:
            return 0
        res = 0
        for i in range(999, n):
            res += 1
        return res


    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)

obj = Solution()
n = 100_000
print(obj.countCommas(n))
