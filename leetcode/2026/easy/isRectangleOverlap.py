import math


class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # 0 - xMin, 1 - xMax, 2 - yMin, 3 - yMax
        one_x_y = [min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)]
        two_x_y = [min(x3, x4), max(x3, x4), min(y3, y4), max(y3, y4)]
        
        if not (
            one_x_y[0] <= two_x_y[1] and one_x_y[1] >= two_x_y[0] and
            one_x_y[2] <= two_x_y[3] and one_x_y[3] >= two_x_y[2]
        ):
            return False

        res_x_y_left = (max(one_x_y[0], two_x_y[0]), max(one_x_y[2], two_x_y[2]))
        res_x_y_right = (min(one_x_y[1], two_x_y[1]), min(one_x_y[3], two_x_y[3]))

        S = (res_x_y_right[0] - res_x_y_left[0]) * (res_x_y_right[1] - res_x_y_left[1])
        return S > 0



obj = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(obj.isRectangleOverlap(rec1, rec2))
