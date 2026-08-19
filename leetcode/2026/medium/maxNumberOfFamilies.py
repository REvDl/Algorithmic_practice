from socket import if_indextoname
from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        set_reserve = defaultdict(set)
        for row, seat in reservedSeats:
          set_reserve[row].add(seat)
        res = (n - len(set_reserve)) * 2
        for row, seats in set_reserve.items():
          left = seats.isdisjoint({2,3,4,5})
          right = seats.isdisjoint({6,7,8,9})
          mid = seats.isdisjoint({4,5,6,7})
          if left and right:
            res += 2
          elif left or right or mid:
            res += 1
        return res
      
        



obj = Solution()
n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
print(obj.maxNumberOfFamilies(n, reservedSeats))