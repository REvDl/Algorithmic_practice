from typing import List


class Solution_2:
	def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
		ans = [[0] * k for _ in range(k)]
		for i in range(x, x + k):
			for j in range(y, y + k):
				ans[i - x][j - y] = grid[i][j]
		ans = ans[::-1]
		for i in range(x, x + k):
			for j in range(y, y + k):
				grid[i][j] = ans[i - x][j - y]
		return grid



class Solution:
	def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
		up = x
		down = x + k - 1
		while up < down:
			u = grid[up]
			d = grid[down]
			for j in range(y, y + k):
				u[j], d[j] = d[j], u[j]
			up += 1
			down -= 1
		return grid
obj = Solution()
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 1
y = 0
k = 3
print(obj.reverseSubmatrix(arr, x, y, k))
