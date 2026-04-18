class Solution:
	@staticmethod
	def _reverse_int(num: int) -> int:
		res = 0
		while num > 0:
			res = res * 10 + num % 10
			num //= 10
		return res





	def mirrorDistance(self, n: int) -> int:
		return abs(n - Solution._reverse_int(n))