import math
from typing import List

class Solution:
	def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
		left, right = 0, 10 ** 17
		while left < right:
			total = 0
			mid = (left + right) // 2
			for t in workerTimes:
				x = (-1 + math.sqrt(1 + (8 * mid) // t)) // 2
				total += x
			if total >= mountainHeight:
				right = mid
			else:
				left = mid + 1
		return left


import math

import math




#print(10 ** 5)
left2, right2 = 1, 10 ** 5
while left2 < right2:
	mid2 = (left2 + right2) // 2
	#print(mid2)
	right2 = mid2

obj = Solution()
arr = [2,1,2]
mountainHeight = 4
print(obj.minNumberOfSeconds(mountainHeight, arr))