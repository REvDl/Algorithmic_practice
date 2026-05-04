from typing import List


class Solution:

	def rotate_non_in_place(self, matrix: List[List[int]]) -> List[list[int]]:
		n, m = len(matrix), len(matrix[0])
		matrix_rotate = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(n):
			for j in range(0, m):
				matrix_rotate[j][(n - 1) - i] = matrix[i][j]
		return matrix_rotate




	def rotate(self, matrix: List[List[int]]) -> None:
		n, m = len(matrix), len(matrix[0])
		for i in range(n):
			for j in range(i, m):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			matrix[i].reverse()
		for i in range(n):
			print(matrix[i])
		"""
		Do not return anything, modify matrix in-place instead.
		"""


def print_matrix(matrix: List[List[int]]) -> None:
	print("\n")
	for i in matrix:
		print(i)


obj = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
obj.rotate(matrix)