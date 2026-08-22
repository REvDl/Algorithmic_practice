


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_n, prod_n = 0, 1
        num = n
        while num > 0:
            last_num = num % 10
            sum_n += last_num
            prod_n *= last_num
            num//=10
        return n % (sum_n + prod_n) == 0






obj = Solution()
n = 99
print(obj.checkDivisibility(n))
