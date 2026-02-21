class Solution(object):
	def twoSum(self, nums: list[int], target:int):
		result = dict()
		for i, num in enumerate(nums):
			remainder = target - num
			if remainder in result:
				return [result[remainder], i]
			else:
				result[num] = i
		return None









def longest_window(s):
	answer, left, right = 0, 0, 0
	char_set = set()
	while right < len(s):
		c = s[right]
		if c not in char_set:
			char_set.add(c)
			answer = max(answer, right - left + 1)
			right += 1
		else:
			while c in char_set:
				char_set.remove(s[left])
				left += 1
	return answer
