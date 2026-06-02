from typing import List



class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        finish = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_F = landStartTime[i] + landDuration[i]
                water_F = waterStartTime[j] + waterDuration[j]
                
                start_land = max(land_F, waterStartTime[j])
                start_water = max(water_F, landStartTime[i])


                finish = min(start_land + waterDuration[j], start_water + landDuration[i], finish)
        return finish




obj = Solution()
landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]
print(obj.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
