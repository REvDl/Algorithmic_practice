from typing import List


class Solution:
	def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
		left, right = startIndex, startIndex
		n = len(words)
		steps = 0
		while steps < n:
			if words[left] == target:
				return steps
			if words[right] == target:
				return steps
			left = (left - 1) % n
			right = (right + 1) % n
			steps += 1
		else:
			return -1

obj = Solution()
words = ["broccoli", "apple", "banana", "apple", "orange", "walnut", "grape", "peanut"]
target = "apple"
startIndex = 6
print(obj.closestTarget(words, target, startIndex))




# class Solution:
# 	def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
# 		left, right = start, start
# 		n = len(nums)
# 		while left >= 0 or right < n:
# 			if nums[left] == target:
# 				return left - start
# 			if nums[right] == target:
# 				return right - start
# 			left -= 1
# 			left += 1