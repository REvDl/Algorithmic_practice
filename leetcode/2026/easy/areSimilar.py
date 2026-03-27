from typing import List


class Solution:
	def areSimilar(self, mat: List[List[int]], k: int) -> bool:
		rows, cols = len(mat), len(mat[0])
		copy_matrix = [row[:] for row in mat]
		k %= cols
		for itr in range(k):
			result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
			for i in range(rows):
				for j in range(cols):
					if i % 2 == 0:
						source_j = j - 1 if j - 1 >= 0 else cols - 1
						result_matrix[i][j] = mat[i][source_j]
					else:
						source_j = j + 1 if j + 1 < cols else 0
						result_matrix[i][j]  = mat[i][source_j]
			mat = result_matrix
		return mat == copy_matrix



	def areSimilar_v2(self, mat: List[List[int]], k: int) -> bool:
		rows, cols = len(mat), len(mat[0])
		k %= cols
		if k == 0:
			return True
		for i in range(rows):
			for j in range(cols):
				if mat[i][j] != mat[i][(j + k) % cols]:
					return False
		return True




obj = Solution()
arr = [[1,2,2],[5,5,5],[6,6,3]]
print(obj.areSimilar(arr, 2))
print(obj.areSimilar_v2(arr, 2))