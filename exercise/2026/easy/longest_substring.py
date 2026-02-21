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
