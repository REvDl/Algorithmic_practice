import math


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_point = [x1, y1]
        if xCenter < x1: closest_point[0] = x1
        elif xCenter < x2: closest_point[0] = xCenter
        else: closest_point[0] = x2
        if yCenter < y1: closest_point[1] = y1
        elif yCenter < y2: closest_point[1] = yCenter
        else: closest_point[1] = y2
        distance_1 = math.dist(closest_point, (xCenter, yCenter))
        if distance_1 <= radius:
            return True
        return False


obj = Solution()
radius = 1
xCenter = 1
yCenter = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1
print(obj.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
