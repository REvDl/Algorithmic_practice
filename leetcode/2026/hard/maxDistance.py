from typing import List


class Solution:
	def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
		result = []
		for x,y in points:
			if y == 0:
				result.append(x)
			elif x == side:
				result.append(side + y)
			elif y == side:
				result.append(2 * side + (side - x))
			elif x == 0:
				result.append(3 * side + (side - y))
		result.sort()
		def check_distance(distance:int):
			for start_index in range(min(len(result), k)):
				count = 1
				last_dot = result[start_index]
				first_dot = result[start_index]
				for i in range(start_index + 1, len(result)):
					if (result[i] - last_dot) >= distance:
						count += 1
						last_dot = result[i]
						if count == k: break
				if count == k:
					if (4 * side) - (last_dot - first_dot) >= distance:
						return True
			return False
		left = 1
		right = side
		ans = 0
		while left <= right:
			mid = (left + right) // 2
			if check_distance(mid):
				ans = mid
				left = mid + 1
			else:
				right = mid - 1
		return ans

obj = Solution()
side = 2
points = [[0,2],[2,0],[2,2],[0,0]]
k = 4
print(obj.maxDistance(side, points, k))
