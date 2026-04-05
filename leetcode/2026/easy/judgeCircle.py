class Solution:
	def judgeCircle_v1(self, moves: str) -> bool:
		counter = {"R": 0, "L": 0, "U": 0, "D":0}
		for i in moves:
			if i == "R":
				counter["R"] += 1
			elif i == "L":
				counter["L"] += 1
			elif i == "U":
				counter["U"] += 1
			elif i == "D":
				counter["D"] += 1
		return counter["L"] == counter["R"] and counter["U"] == counter["D"]

	def judgeCircle(self, moves: str) -> bool:
		L, R, U, D = moves.count("L"), moves.count("R"), moves.count("U"), moves.count("D")
		return L == R and U == D


obj = Solution()
moves = "UD"
print(obj.judgeCircle(moves))