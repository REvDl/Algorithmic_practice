class Solution:
	def bitwiseComplement(self, n: int) -> int:
		result = bin(n)[2::]
		result = result.replace("1", "2").replace("0", "1").replace("2", "0")
		return int(result, 2)



	def bitwiseComplement_v2(self, n: int) -> int:
		x = n
		mask = 0
		while x:
			mask = (mask << 1) | 1
			x>>= 1
		return mask ^ n


n = 10
obj = Solution()
print(obj.bitwiseComplement(n))
print(obj.bitwiseComplement_v2(n))