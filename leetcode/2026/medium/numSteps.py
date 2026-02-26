class Solution_v1:
	def numSteps_v1(self, s: str) -> int:
		"""Crutch option"""
		steps = 0
		binary_num = int(s, 2)
		while binary_num != 1:
			steps += 1
			if binary_num % 2 == 0:
				binary_num /= 2
			else:
				binary_num += 1
		return steps


class Solution_v2:
	def numSteps_v2(self, s: str) -> int:

		"""I'm not sure about that"""
		steps = 0
		while s != "1":
			steps += 1
			if s[-1] == "0":
				s = s[:-1]
			else:
				s = list(s)
				for i in range(len(s) - 1, -1, -1):
					if s[i] == "1":
						s[i] = "0"
					else:
						s[i] = "1"
						break
				else:
					s.insert(0, "1")
			s = "".join(s)
		return steps



class Solution_v3:
	def numStepsv3(self, s: str) -> int:
		s = list(s)
		steps = 0
		while len(s) > 1:
			steps += 1
			if s[-1] == "0":
				s.pop()
			else:
				for i in range(len(s)-1, -1, -1):
					if s[i] == "1":
						s[i] = "0"
					else:
						s[i] = "1"
						break
				else:
					s.insert(0, "1")
		return steps


class Solution:
	def numSteps(self, s: str) -> int:
		steps = 0
		carry = 0
		N = len(s)
		for i in range(N - 1, 0, -1):
			digit = int(s[i]) + carry
			if digit % 2 == 1:
				steps += 2
				carry = 1
			else:
				steps += 1
		return steps + carry

obj = Solution()
print(obj.numSteps("1111011110000011100000110001011011110010111001010111110001"))
