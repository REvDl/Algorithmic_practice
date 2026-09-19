

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        coords_circle = [(xCenter + radius, yCenter), (xCenter, yCenter + radius), (xCenter - radius, yCenter), (xCenter, yCenter - radius)]
        coords_square = [(x1, y1), (x2, y2), (x2, y1), (x1, y2)]
        for circle in coords_circle:
            for square in coords_square:
                if circle[0] <= square[0] and circle[1] <= square[1]:
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
