




class Solution:
    def _prod_digits(self, n: int) -> int:
        if n == 0: return 0
        prod = 1
        while n > 0:
            prod *= n % 10
            n //= 10
        return prod


    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 1000):
            res = self._prod_digits(i)
            if res % t == 0:
                return i


obj = Solution()
n = 50
t = 3
print(obj.smallestNumber(n, t))
