


class ProductOfNumbers:

    def __init__(self):
        self.P = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.P = [1]
        else:
            if self.P:
                self.P.append(self.P[-1] * num)
            else:
                self.P.append(num)
    def getProduct(self, k: int) -> int:
        if k >= len(self.P):
            return 0
        return self.P[-1] // self.P[len(self.P) - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.P)
assert obj.getProduct(2) == 20
assert obj.getProduct(3) == 40
assert obj.getProduct(4) == 0
obj.add(8)
assert obj.getProduct(2) == 32
