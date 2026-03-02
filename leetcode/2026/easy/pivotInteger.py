class Solution:
	def pivotInteger(self, n: int):
		total_sum = (n * (n + 1)) / 2
		left_sum = 0
		for i in range(1, n + 1):
			left_sum += i
			sum_x = total_sum - left_sum + i
			if sum_x == left_sum:
				return i
		return -1




obj = Solution()
print(obj.pivotInteger(8))
