from collections import Counter


class Solution:
	def furthestDistanceFromOrigin_V1(self, moves: str) -> int:
		L, R = moves.count("L"), moves.count("R")
		if L > R:
			moves = moves.replace("_", "L")
		else:
			moves = moves.replace("_", "R")
		return abs(moves.count("L") - moves.count("R"))

	def furthestDistanceFromOrigin_v2(self, moves: str) -> int:
		return abs(moves.count("L") - moves.count("R")) + moves.count("_")



	def furthestDistanceFromOrigin(self, moves: str) -> int:
		count = Counter(moves)
		return abs(count["L"] - count["R"]) + count["_"]



obj = Solution()
moves = "L_RL__R"
print(obj.furthestDistanceFromOrigin(moves))