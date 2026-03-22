from typing import List


class Solution:
	def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
		for _ in range(4):
			if mat == target:
				return True
			for i in range(len(mat)):
				for j in range(i + 1, len(mat)):
					mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
			for i in range(len(mat)):
				mat[i].reverse()
		return False





obj = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
print(obj.findRotation(mat, target))
