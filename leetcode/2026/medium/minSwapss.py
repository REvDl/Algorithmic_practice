from typing import List


class Solution:
	def minSwaps(self, grid: List[List[int]]) -> int:
		n = len(grid)
		zeros = []
		steps = 0
		for row in grid:
			count = 0
			for j in range(n - 1, -1, -1):
				if row[j] == 0:
					count += 1
				else:
					break
			zeros.append(count)

		for i in range(n):
			needed = n - 1 - i
			j = i
			while j < n and zeros[j] < needed:
				j += 1
			if j == n:
				return -1
			steps += j - i
			while j > i:
				zeros[j] = zeros[j - 1]
				j -= 1
		return steps




ojb = Solution()
print(ojb.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))


# [1,0,0]
# [1,1,0]
# [0,0,1]
