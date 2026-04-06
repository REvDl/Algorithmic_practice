from bisect import bisect_left, bisect_right
from typing import List


class Solution:
	def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
		robots_sorted = []
		for i in range(len(robots)):
			robots_sorted.append([robots[i], distance[i], i])
		robots_sorted.sort()
		robots_sorted.insert(0, [-float('inf'), 0])
		robots_sorted.append([float('inf'), 0])
		walls.sort()
		L, R = [], []
		for i in range(1, len(robots_sorted) - 1):
			curr = robots_sorted[i][0]
			dist = robots_sorted[i][1]

			left_robot = max(robots_sorted[i - 1][0], curr - dist)
			right_robot = min(robots_sorted[i + 1][0], curr + dist)

			idx_l_start = bisect_left(walls, left_robot)
			idx_l_end = bisect_right(walls, curr)
			count_l = idx_l_end - idx_l_start

			idx_r_start = bisect_left(walls, curr)
			idx_r_end = bisect_right(walls, right_robot)
			count_r = idx_r_end - idx_r_start

			L.append(count_l)
			R.append(count_r)
		f_left = L[0]
		f_right = R[0]
		for i in range(1, len(robots)):
			best_before = max(f_left, f_right)
			f_left = best_before + L[i]
			f_right = best_before + R[i]
		return max(f_left, f_right)



obj = Solution()
robots = [4]
distance = [3]
walls = [1,10]
print(obj.maxWalls(robots, distance, walls))
#Output: 1


robots = [10,2]
distance = [5,1]
walls = [5,2,7]
print(obj.maxWalls(robots, distance, walls))
#Output: 3