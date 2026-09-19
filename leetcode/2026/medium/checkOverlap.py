import math


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        position_x = max(x1, min(xCenter, x2))
        position_y = max(y1, min(yCenter, y2))
        distance = math.dist((position_x, position_y), (xCenter, yCenter))
        return distance <= radius


obj = Solution()
radius = 1
xCenter = 1
yCenter = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1
print(obj.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
