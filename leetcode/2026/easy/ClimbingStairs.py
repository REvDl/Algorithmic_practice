class Solution:
	def climbStairs(self, n: int) -> int:
		#создаем массив вида (при n = 4) [0, 0, 0, 0, 0]
		dp = [0] * (n + 1)
		#первый элемент как первый шаг, типа в любом случае первый шаг будет 1
		dp[0] = 1
		for i in range(1, n + 1):
			dp[i] += dp[i - 1]
			#если i > 2, значит можем прибавить 2 вместо 1
			if i >= 2:
				dp[i] += dp[i - 2]
		#возвращаем число с индексом n
		return dp[n]



obj = Solution()
print(obj.climbStairs(38))