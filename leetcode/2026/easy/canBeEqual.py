class Solution:
	def canBeEqual(self, s1: str, s2: str) -> bool:
		not_even1 = sorted([s1[1], s1[3]])
		not_even2 = sorted([s2[3], s2[1]])
		even = sorted([s1[0], s1[2]])
		even2 = sorted([s2[2], s2[0]])
		return not_even1 == not_even2 and even == even2



obj = Solution()
s1 = "bnxw"
s2 = "bwxn"
print(obj.canBeEqual(s1,s2))