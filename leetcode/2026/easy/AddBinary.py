class Solution:
	def addBinary(self, a: str, b: str) -> str:
		result = int(a, 2) + int(b, 2)
		return bin(result)[2:]

large_a = "1" * 100000000
obj = Solution()
print(obj.addBinary(large_a, "1"))