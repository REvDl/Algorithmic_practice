class Fancy:

	def __init__(self):
		self.mod = 10 ** 9 + 7
		self.fancy = []
		self.m = 1
		self.a = 0


	def append(self, val: int) -> None:
		x = (val - self.a + self.mod) % self.mod
		self.fancy.append(x * pow(self.m, self.mod -2, self.mod) % self.mod)

	def addAll(self, inc: int) -> None:
		self.a = (self.a + inc) % self.mod

	def multAll(self, m: int) -> None:
		self.m = (self.m * m) % self.mod
		self.a = (self.a * m) % self.mod
	def getIndex(self, idx: int) -> int:
		return (self.fancy[idx] * self.m + self.a) % self.mod if len(self.fancy) > idx else -1




# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)


obj = Fancy()
obj.append(2)
obj.addAll(3)
#5, 7
obj.append(7)
obj.multAll(2)
#10, 14
obj.addAll(3)
#13, 17
obj.append(10)
#13, 17, 10
obj.multAll(2)
#26, 34, 20
print(obj.getIndex(0))
print(obj.getIndex(1))
print(obj.getIndex(2))

