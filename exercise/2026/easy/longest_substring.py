def longest_substring(s):
	answer = 0
	for left in range(len(s)):
		for right in range(left, len(s)):
			is_accept = True
			char_set = set()
			for i in range(left, right+1):
				if s[i] in char_set:
					is_accept = False
					break
				char_set.add(s[i])
			if is_accept and answer < right - left +1:
				answer = right - left + 1
	return answer

