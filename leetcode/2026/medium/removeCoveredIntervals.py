from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        res = n
        max_r = intervals[0][-1]
        for i in range(1, n):
            if intervals[i][1] > max_r:
                max_r = intervals[i][1]
            else:
                res -= 1
        return res



obj = Solution()
intervals = [[[1,4],[2,3]], [[1,4],[3,6],[2,8]], [[1, 5], [2, 3], [2, 4]], [[3,10],[4,10],[5,11]]]
for interval in intervals:
    print(obj.removeCoveredIntervals(interval))
