class Solution:
	def checkStrings(self, s1: str, s2: str) -> bool:
		even1 = [n for i, n in enumerate(s1) if i % 2 == 0]
		even2 = [n for i, n in enumerate(s2) if i % 2 == 0]
		not_even1 = [n for i, n in enumerate(s1) if i % 2 != 0]
		not_even2 = [n for i, n in enumerate(s2) if i % 2 != 0]
		return sorted(even1) == sorted(even2) and sorted(not_even1) == sorted(not_even2)


	def checkStrings_v2(self, s1: str, s2: str) -> bool:
		return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])



obj = Solution()
s1 = "abe"
s2 = "abe"
print(obj.checkStrings(s1, s2))
print(obj.checkStrings_v2(s1, s2))