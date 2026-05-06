from typing import List


class Solution:
	def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
		n, m = len(boxGrid), len(boxGrid[0])
		for i in range(n):
			bottom = m - 1
			for j in range(m - 1, -1, -1):
				if boxGrid[i][j] == "*":
					bottom = j - 1
				elif boxGrid[i][j] == "#":
					boxGrid[i][bottom] = "#"
					if j != bottom:
						boxGrid[i][j] = "."
					bottom -= 1
		matrix_rotate = [["." for _ in range(n)] for _ in range(m)]
		for i in range(n):
			for j in range(0, m):
				matrix_rotate[j][(n - 1) - i] = boxGrid[i][j]
		return matrix_rotate





obj = Solution()
boxgrid = [["#",".","#"]]
print(obj.rotateTheBox(boxgrid))