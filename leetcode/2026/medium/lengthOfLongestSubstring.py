class Solution(object):
	def lengthOfLongestSubstring(self, s):
		answer, right, left = 0, 0, 0
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



obj = Solution()
string_func = "pwwkew"
print(obj.lengthOfLongestSubstring(string_func))