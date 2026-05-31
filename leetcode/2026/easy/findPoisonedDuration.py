from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i + 1] - timeSeries[i]
            if diff >= duration:
                result += duration
            else:
                result += diff
        return result + duration

