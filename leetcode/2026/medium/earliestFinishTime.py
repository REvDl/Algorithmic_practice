from typing import List

class Solution:
    def earliestFinishTime_yesterday(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

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


    def get_earliest_end(self, StartTime: List[int], Duration: List[int]) -> int:
        return min(StartTime[i] + Duration[i] for i in range(len(StartTime)))

    def solve_one_way(self, FirstStartTime: List[int], FirstDuration: List[int], SecondStartTime: List[int],
                             SecondDuration: List[int]) -> int:
        min_end = self.get_earliest_end(FirstStartTime, FirstDuration)
        earliest_end = float("inf")
        for i, start_time in enumerate(SecondStartTime):
            start = min_end if min_end > start_time else start_time
            current_finish = start + SecondDuration[i]
            if current_finish < earliest_end:
                earliest_end = current_finish
        return earliest_end

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        return min(self.solve_one_way(landStartTime, landDuration, waterStartTime, waterDuration),
                   self.solve_one_way(waterStartTime, waterDuration, landStartTime, landDuration)
        )
