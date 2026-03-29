def generate_lcp(word: str) -> list[list[int]]:
	n = len(word)
	# Твой код здесь
	dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(n-1, -1, -1):
		for j in range(n-1, -1, -1):
			if word[i] == word[j]:
				dp[i][j] = dp[i+1][j+1] + 1
			else:
				dp[i][j] = 0
	return [row[:n] for row in dp[:n]]



word = "ababa"
print(generate_lcp(word))