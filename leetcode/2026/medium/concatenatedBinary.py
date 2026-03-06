class Solution:
	def concatenatedBinary(self, n: int) -> int:
		result = []
		for i in range(1, n+1):
			result.append(bin(i)[2::])
		result_end = "".join(result)
		result_finally = int(result_end, 2) % (10**9 + 7)
		return result_finally


obj = Solution()
print(obj.concatenatedBinary(1000000))