class Solution(object):
	def longestCommonPrefix(self, strs):
		prefix = ""
		if not strs:
			return prefix
		min_len = min(strs, key=len)
		for i in range(len(min_len)):
			char = strs[0][i]
			if all(s[i] == char for s in strs):
				prefix += char
			else:
				break
		return prefix



strs = ["fasdasdasdasd","flow","fasdasd"]
ojb = Solution()
print(ojb.longestCommonPrefix(strs))
print(min(['flower', 'flow', 'flight'], key=len))