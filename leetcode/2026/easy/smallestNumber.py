




class Solution:
    def _prod_digits(self, n: int) -> int:
        if n == 0: return 0
        prod = 1
        while n > 0:
            prod *= n % 10
            n //= 10
        return prod


    def smallestNumber_v1(self, n: int, t: int) -> int:
        for i in range(n, 1000):
            res = self._prod_digits(i)
            if res % t == 0:
                return i

    def smallestNumber_v2(self, n: int, t: int) -> int:
        step = 0
        while step <= 10:
            num = n + step
            res = self._prod_digits(num)
            if res % t == 0:
                return num
            step += 1


    def smallestNumber_v3(self, n: int, t: int) -> int:
        for i in range(n, n+11):
            if self._prod_digits(i) % t == 0:
                return i

obj = Solution()
n = 20
t = 2
print(obj.smallestNumber_v3(n, t))

