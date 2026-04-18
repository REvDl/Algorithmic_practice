


class Solution:
	def longestPalindrome(self, s: str) -> str:
		max_len = 0
		result = []
		n = len(s)
		for i in range(n):
			for j in range(i, n):
				substring = s[i:j]
				if substring == substring[::-1]:
					if len(substring) > max_len:
						result.append(substring)
						max_len = len(substring)
		return max(result, key=len)

obj = Solution()
s = "cbbd"
print(obj.longestPalindrome(s))