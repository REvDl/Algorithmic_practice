

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_min = minutes * 6
        angle_hour = (hour%12 * 30) + (minutes * 0.5)
        diff = abs(angle_hour - angle_min)
        return min(diff, 360-diff)
