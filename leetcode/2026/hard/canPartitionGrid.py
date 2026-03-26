from typing import List, Counter


class Solution:
	def canPartitionGrid(self, grid: List[List[int]]) -> bool:
		def check_grid(grid:List[List[int]]):
			rows, cols = len(grid), len(grid[0])
			rows_sum = [sum(grid[r]) for r in range(rows)]
			total_sum = sum(rows_sum)
			current_sum = 0
			for r in range(rows-1):
				current_sum += rows_sum[r]
				top_sum = current_sum
				bottom_sum = total_sum - top_sum
				diff = abs(top_sum - bottom_sum)
				if diff == 0: return True
				if top_sum > bottom_sum:
					if r == 0:
						if diff == grid[r][0] or diff == grid[r][cols - 1]: return True
					elif cols == 1:
						if diff == grid[0][0] or diff == grid[r][0]: return True
					else:
						if diff in set(grid[0]) or diff in set(grid[r]): return True
						for i in range(r + 1):
							if diff == grid[i][0] or grid[i][cols-1]: return True
				else:
					rows_below = (rows - 1) - r
					if rows_below == 1:
						if diff == grid[r+1][0] or diff == grid[r+1][cols - 1]: return True
					elif cols == 1:
						if diff == grid[0][0] or diff == grid[r+1][0]: return True
					else:
						if diff in set(grid[r+1]) or diff in set(grid[rows-1]): return True
						for i in range(r + 1, rows):
							if diff == grid[i][0] or diff == grid[r][cols-1]: return True
			return False
		transposed = [list(row) for row in zip(*grid)]
		check_norm = check_grid(grid)
		check_transposed = check_grid(transposed)
		return check_norm or check_transposed



	def canPartitionGrid_SUKA_TWO_VARIANT(self, grid: List[List[int]]) -> bool:
		def check_grid(matrix):
			R, C = len(matrix), len(matrix[0])
			row_sums = [sum(row) for row in matrix]
			total_sum = sum(row_sums)
			bottom_counts = Counter()
			for r in range(R):
				bottom_counts.update(matrix[r])

			top_counts = Counter()
			current_top_sum = 0

			for r in range(R - 1):
				row = matrix[r]
				current_top_sum += row_sums[r]
				for val in row:
					top_counts[val] += 1
					bottom_counts[val] -= 1
					if bottom_counts[val] == 0: del bottom_counts[val]

				sum1, sum2 = current_top_sum, total_sum - current_top_sum
				diff = sum1 - sum2

				if diff == 0: return True
				if diff > 0:
					if r > 0 and C > 1:
						if diff in top_counts: return True
					else:  # Секция - одна строка или один столбец
						if r == 0:  # Одна строка
							if diff == row[0] or diff == row[C - 1]: return True
						elif C == 1:  # Один столбец
							# Проверяем только края текущего куска столбца
							if diff == matrix[0][0] or diff == matrix[r][0]: return True

				# Если нужно вычесть из НИЖНЕЙ части
				elif diff < 0:
					target = -diff
					rows_below = (R - 1) - r
					if rows_below > 1 and C > 1:
						if target in bottom_counts: return True
					else:
						if rows_below == 1:  # Одна строка внизу
							last_row = matrix[R - 1]
							if target == last_row[0] or target == last_row[C - 1]: return True
						elif C == 1:  # Один столбец внизу
							if target == matrix[r + 1][0] or target == matrix[R - 1][0]: return True
			return False

		# Твоя идея с транспонированием — топ, оставляем
		if check_grid(grid): return True
		transposed = [list(t) for t in zip(*grid)]
		return check_grid(transposed)


obj = Solution()
arr = [[5,5,6,2,2,2]]
print(obj.canPartitionGrid(arr))