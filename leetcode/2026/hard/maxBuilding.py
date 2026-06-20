from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n-1])
        restrictions.sort(key=lambda x: x[0])
        max_val = 0
        for i in range(len(restrictions) - 1):
            restrictions[i+1][1] = min(restrictions[i+1][1], restrictions[i][1] + (restrictions[i+1][0] - restrictions[i][0]))
        for i in range(len(restrictions) -2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))
        for i in range(len(restrictions) -1 ):
            peak = (restrictions[i][1] + restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0])) // 2
            max_val = max(max_val, peak)
        return max_val



obj = Solution()
n = 5
restrictions = [[5,3],[2,5],[7,4],[10,3]]
print(obj.maxBuilding(n, restrictions))

