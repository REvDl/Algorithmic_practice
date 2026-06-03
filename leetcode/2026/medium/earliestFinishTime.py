from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        minLand = min(landStartTime[i] + landDuration[i] for i in range(len(landStartTime)))
        minWater = min(waterStartTime[i] + waterDuration[i] for i in range(len(waterStartTime)))

        finish_water = float("inf")
        finish_land = float("inf")

        for i in range(len(waterStartTime)):
            start_water = max(minLand, waterStartTime[i])
            finish_water = min(start_water + waterDuration[i], finish_water)

        for i in range(len(landStartTime)):
            start_land = max(minWater, landStartTime[i])
            finish_land = min(start_land + landDuration[i], finish_land)

        return min(finish_land, finish_water)

    def earliestFinishTime_2(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                             waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        minLand = min(landStartTime[i] + landDuration[i] for i in range(n))
        minWater = min(waterStartTime[i] + waterDuration[i] for i in range(m))

        finish_land = float("inf")
        finish_water = float("inf")

        for i in range(n):
            start_land = max(minWater, landStartTime[i])
            finish_land = min(start_land + landDuration[i], finish_land)

        for j in range(m):
            start_water = max(minLand, waterStartTime[j])
            finish_water = min(start_water + waterDuration[j], finish_water)
        return min(finish_water, finish_land)
