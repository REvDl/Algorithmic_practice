from typing import List


class Robot:


	def __init__(self, width: int, height: int):
		self.w = width
		self.h = height
		self.x = 0
		self.y = 0
		self.direction = "East"

	def step(self, num: int) -> None:
		P = 2 * (self.w + self.h - 2)
		num %= P
		if num == 0:
			num = P
		while num:
			if self.direction == "East":
				border = min(self.x + num, self.w - 1)
				diff = border - self.x
				num -= diff
				if num == 0:
					self.x = border
				else:
					self.x = border; self.direction = "North"

			elif self.direction == "West":
				border = max(self.x - num, 0)
				diff = self.x - border
				num -= diff
				if num == 0:
					self.x = border
				else:
					self.x = border
					self.direction = "South"


			elif self.direction == "North":
				border = min(self.y + num, self.h - 1)
				diff = border - self.y
				num -= diff
				if num == 0: self.y = border
				else: self.y = border;  self.direction = "West"


			elif self.direction == "South":
				border = max(self.y - num, 0)
				diff = self.y - border
				num -= diff
				self.y = border
				if num > 0:
					self.direction = "East"



	def getPos(self) -> List[int]:
		return [self.x, self.y]
	def getDir(self) -> str:
		return self.direction




# Your Robot object will be instantiated and called as such:
width, height, num = 6, 3, 2
obj = Robot(width, height)
obj.step(num)
param_2 = obj.getPos()
param_3 = obj.getDir()
print(param_2)
print(param_3)