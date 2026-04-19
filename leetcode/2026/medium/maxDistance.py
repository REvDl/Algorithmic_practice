from typing import List


class Solution:
	def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
		i, j = 0, 0
		max_diss = 0
		while i < len(nums1):
			while j < len(nums2) and nums1[i] <= nums2[j]:
				j += 1
			if j < i: j = i
			max_diss = max(max_diss, j - i - 1)
			i += 1
		return max_diss

obj = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
print(obj.maxDistance(nums1, nums2))