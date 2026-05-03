class Solution:
	def rotateString_v1(self, s: str, goal: str) -> bool:
		n = len(s)
		for _ in range(n):
			if s == goal:
				return True
			s = s[-1] + s[:-1]
			print(s)
		return False


	def rotateString(self, s:str, goal:str) -> bool:
		return len(s) == len(goal) and goal in (s + s)




obj = Solution()
s = "abcde"
goal = "cdeab"
print(obj.rotateString(s, goal))