from idlelib.debugobj import myrepr
from typing import List


class Solution:
	def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
		direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
		set_obs = {tuple(o) for o in obstacles}
		max_dist = 0
		curr_dr = 0
		x, y = 0, 0
		for command in commands:
			if command == -1:
				curr_dr = (curr_dr + 1) % 4
			elif command == -2:
				curr_dr = (curr_dr + 3) % 4
			else:
				dx, dy = direction[curr_dr]
				for _ in range(command):
					nx, ny = x + dx, y + dy
					if (nx, ny) in set_obs:
						break
					x, y = nx, ny
					if x ** 2 + y ** 2 > max_dist:
						max_dist = x ** 2 + y ** 2

		return max_dist
	def robotSim_vrite_again(self, commands: List[int], obstacles: List[List[int]]) -> int:
		direction, set_obs = [[0, 1], [1, 0], [0, -1], [-1, 0]], {tuple(o) for o in obstacles}
		curr_dr, max_dist = 0, 0
		x, y = 0, 0
		for command in commands:
			if command == -1:
				curr_dr = (curr_dr + 1) % 4
			elif command == -2:
				curr_dr = (curr_dr + 3) % 4
			else:
				dx, dy = direction[curr_dr]
				for _ in range(command):
					nx, ny = x + dx, y + dy
					if (nx, ny) in set_obs:
						break
					x, y = nx, ny
					if x ** 2 + y ** 2 > max_dist:
						max_dist = x ** 2 + y ** 2
		return max_dist
obj = Solution()
commands = [[4,-1,3], [4,-1,4,-2,4]]
obstacles = [[], [[2,4]]]

for i in range(len(commands)):
	try:
		print(f"1: {obj.robotSim(commands[i], obstacles[i])}")
		print(f"2: {obj.robotSim_vrite_again(commands[i], obstacles[i])}")
	except IndexError:
		pass