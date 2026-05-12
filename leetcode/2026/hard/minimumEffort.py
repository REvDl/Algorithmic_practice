from typing import List

class Solution:
	def minimumEffort(self, tasks: List[List[int]]) -> int:
		tasks.sort(key=lambda x: x[0] - x[1])
		energy = 0
		current = 0
		for task in tasks:
			diff = task[1] - energy
			if energy < task[1]:
				energy += diff
				current += diff
			energy -= task[0]
		return current



obj = Solution()
tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
print(obj.minimumEffort(tasks))


