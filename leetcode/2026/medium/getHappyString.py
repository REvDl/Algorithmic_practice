from itertools import product


class Solution:
	def getHappyString(self, n: int, k: int) -> str:
		chars = ["a", "b", "c"]
		count = 0
		for p in product(chars, repeat=n):
			s = "".join(p)
			if all(s[i] != s[i + 1] for i in range(len(s) - 1)):
				count += 1
				if count == k:
					return s
		return ""



class Solution_2:
	def getHappyString(self, n:int, k: int) -> str:
		chars = ["a", "b", "c"]
		count = 0
		def generate(s:str, n:int, chars):
			nonlocal count
			pass


obj = Solution()
obj_2 = Solution_2()
print(obj.getHappyString(3, 9))
print(obj.getHappyString(3, 9))