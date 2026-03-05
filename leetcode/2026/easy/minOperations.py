class Solution:
	def minOperations(self, s: str) -> int:
		count0 = 0
		n = len(s)
		for key, value in enumerate(s):
			if (key % 2 == 0 and value != "0") or (key % 2 != 0 and value != "1"):
				count0 += 1
		return min(n - count0, count0)


obj = Solution()
print(obj.minOperations("010011110001100110010101000101010100100101001100010010101111000"))