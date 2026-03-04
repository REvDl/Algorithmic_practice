from typing import List


class Solution:
	def numSpecial(self, mat: List[List[int]]):
		m = len(mat)
		n = len(mat[0])
		count = 0
		for i in range(len(mat)):
			for j in range(len(mat[i])):
				if (
					mat[i][j] == 1
					and all(mat[i][col] == 0 for col in range(n) if col != i)
					and all(mat[i][row] == 0 for row in range(m) if row != j)
				):
					count += 1
		return count



class Solution_v2:
	def numSpecial(self, mat: List[List[int]]):
		row_count = [sum(row) for row in mat]
		col_count = [sum(col) for col in mat[0]]
		for i in range(len(mat)):
			sum_i = 0
			for j in range(len(mat[i])):
				pass
		return row_count, "\n", col_count


mat = [
	[1,0,0],
	[0,0,1],
	[1,0,0]]
obj = Solution_v2()
print(obj.numSpecial(mat))
