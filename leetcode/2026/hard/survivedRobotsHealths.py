from typing import List


class Solution:
	def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
		robots, stack = [], []
		for i in range(len(positions)):
			#0 - position, 1 - health, 2 - direction, 4 - serial number
			robots.append([positions[i], healths[i], directions[i], i])
		robots.sort()
		for current_robot in robots:
			if current_robot[2] == "R":
				stack.append(current_robot)
			else:
				while stack and stack[-1][2] == "R":
					if stack[-1][1] < current_robot[1]:
						stack.pop()
						current_robot[1] -= 1
					elif stack[-1][1] > current_robot[1]:
						stack[-1][1] -= 1
						current_robot[1] = 0
						break
					else:
						stack.pop()
						current_robot[1] = 0
						break
				if current_robot[1] > 0:
					stack.append(current_robot)
		stack.sort(key= lambda x : x[3])
		return [robot[1] for robot in stack]



obj = Solution()
positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
print(obj.survivedRobotsHealths(positions, healths, directions))
