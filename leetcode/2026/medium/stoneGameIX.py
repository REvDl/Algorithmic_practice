from typing import List
from collections import defaultdict


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones_diff = defaultdict(int)
        for stone in stones:
            diff = stone % 3
            stones_diff[diff] += 1
        count_zero = stones_diff[0]
        count_one = stones_diff[1]
        count_two = stones_diff[2]
        if count_zero % 2 == 0:
            if count_one >= 1 and count_two >= 1:
                return True
            else:
                return False
        else:
            if count_one - count_two > 1 or count_two - count_one > 2:
                return True
            else:
                return False


obj = Solution()
stones = [5,1,2,4,3,7]
print(obj.stoneGameIX(stones))
