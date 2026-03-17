class Solution:
	def largestSubmatrix(self, matrix: list[list[int]]) -> int:
		rows = len(matrix)
		cols = len(matrix[0])
		ans = 0
		for i in range(rows):
			for j in range(cols):
				if matrix[i][j] == 1 and i > 0:
					matrix[i][j] += matrix[i-1][j]
			curr_row = sorted(matrix[i], reverse=True)
			for k in range(cols):
				# ans = max(0, 3 * 1)
				# ans = max(3, 2 * 2)
				# ans = max(4, 0 * 3)
				ans = max(ans, curr_row[k] * (k + 1))
		return ans




obj = Solution()
arr = [[0,0,1],[1,1,1],[1,0,1]]
print(obj.largestSubmatrix(arr))
print(obj.largestSubmatrix([[1,0,1,0,1]]))

"""

0, 0, 1
1, 1, 1
1, 0, 1

[0, 0, 1]
[1, 1, 2]
[2, 0, 3]



1, 1, 1, 0, 0


1, 1, 0
1, 0, 1

"""