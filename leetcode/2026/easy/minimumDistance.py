from typing import List


class Solution:
	def minimumDistance(self, nums: List[int]) -> int:
		result_distance = []
		n = len(nums)
		for i in range(n):
			for j in range(i + 1, n):
				for k in range(j + 1, n):
					if nums[i] == nums[j] == nums[k]:
						dist = abs(i - j) + abs(j - k) + abs(k - i)
						result_distance.append(dist)
		return min(result_distance) if result_distance else -1




obj = Solution()
nums = [1,2,1,1,3]
#expected 6
print(obj.minimumDistance(nums))

nums = [1]
print(obj.minimumDistance(nums))


nums = [5,5,5,2,5]
print(obj.minimumDistance(nums))