class Solution(object):
	def hasAllCodes(self, s, k):
		my_set = set()
		for i in range(len(s) - k + 1):
			my_set.add(s[i:i+k])
		return len(my_set) == 2**k


string_code = "0110"
k_len = 2


obj = Solution()
print(obj.hasAllCodes(string_code, k_len))
# print(my_func(string_code, k_len))