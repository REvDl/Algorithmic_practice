class Solution:
	ROMAN_NUMBERS = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	def romanToInt(self, s: str) -> int:
		result = 0
		for a, b in zip(s, s[1:]):
			if self.ROMAN_NUMBERS[a] < self.ROMAN_NUMBERS[b]:
				result -= self.ROMAN_NUMBERS[a]
			else:
				result += self.ROMAN_NUMBERS[a]
		return result + self.ROMAN_NUMBERS[s[-1]]


obj = Solution()
print(obj.romanToInt("III"))
# 1000, 100, 1000, 10, 100, 1, 5
#если перед числом стоит число, которое меньше его, значит надо отнять его от этого числа, по сути римская IV(4)
#это значит  1 отнять от 5, то есть = 4