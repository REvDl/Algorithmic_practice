class Solution:
	def generateString(self, str1: str, str2: str) -> str:
		n, m = len(str1), len(str2)
		word = [""] * (n + m - 1)
		fix = [False] * (n + m - 1)
		for i in range(n):
			if str1[i] == "T":
				for j in range(m):
					# помечаем что тут занято
					fix[i + j] = True
					if len(word[i + j]) > 0 and word[i + j] != str2[j]:
						return ""
					word[i + j] = str2[j]
		for i in range(len(word)):
			if len(word[i]) <= 0:
				word[i] = "a"
		for i in range(n):
			if str1[i] == "F":
				if "".join(word[i: i + m]) == str2:
					for j in range(m - 1, -1, -1):
						# проверяем, не занято ли условием T
						if not fix[i + j]:
							if word[i + j] == str2[j]:
								word[i + j] = "b" if word[i + j] == "a" else "a"
								break
					else:
						return ""
		return "".join(word)


obj = Solution()
str1 = "TTFFT"
str2 = "fff"
print(obj.generateString(str1, str2))
str1 = "TFTF"
str2 = "abc"
print(obj.generateString(str1, str2))
