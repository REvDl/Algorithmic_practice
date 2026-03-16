from typing import List


class Solution:
	def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
		result_sum = set()
		rows = len(grid)
		cols = len(grid[0])
		for i in range(rows):
			for j in range(cols):
				result_sum.add(grid[i][j])
				k = 1
				while i - k >= 0 and i + k < rows and j - k >= 0 and j + k < cols:
					rhombus_sum = 0
					for x in range(k):
						rhombus_sum += grid[i - k + x][j + x]
						rhombus_sum += grid[i + x][j + k - x]
						rhombus_sum += grid[i + k - x][j - x]
						rhombus_sum += grid[i - x][j - k + x]
					result_sum.add(rhombus_sum)
					k+=1
		return sorted(list(result_sum), reverse=True)[:3]




arr = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
obj = Solution()
print(obj.getBiggestThree(arr))