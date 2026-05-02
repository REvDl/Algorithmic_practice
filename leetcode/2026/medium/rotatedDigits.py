class Solution:
	def rotatedDigits(self, n: int) -> int:
		valid = ["2", "6", "5", "9"]
		invalid = ["3", "4", "7"]
		count = 0
		for i in range(1, n + 1):
			number = str(i)
			if all(x not in invalid for x in number) and any(x in valid for x in number):
				count += 1
		return count


obj = Solution()
print(obj.rotatedDigits(2))