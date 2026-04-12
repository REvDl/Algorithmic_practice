class Solution:
	def minimumDistance(self, word: str) -> int:
		dp = [[float('inf')] * 26 for _ in range(len(word))]

		def get_pos(char: str) -> tuple:
			pos = ord(char) - ord("A")
			return pos // 6, pos % 6

		def distance(char1: str, char2: str) -> int:
			if char1 is None or char2 is None:
				return 0
			x1, y1 = get_pos(char1)
			x2, y2 = get_pos(char2)
			return abs(x1 - x2) + abs(y1 - y2)

		for j in range(26):
			dp[0][j] = 0

		for i in range(len(word) - 1):
			for j in range(26):
				dp[i+1][j] = min(dp[i+1][j], dp[i][j] + distance(word[i], word[i+1]))

				curr_index = ord(word[i]) - ord("A")
				cost = 0 if i == 0 else distance(chr(j + ord("A")), word[i + 1])

				dp[i+1][curr_index] = min(dp[i+1][curr_index], dp[i][j] + cost)
		return int(min(dp[-1]))




obj = Solution()
word = "HAPPY"
print(obj.minimumDistance(word))





