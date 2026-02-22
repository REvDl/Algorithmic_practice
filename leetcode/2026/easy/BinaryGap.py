class Solution(object):
	def binaryGap(self, n):
		grap = 0
		last_index = -1
		binary_n = bin(n)[2:]
		for num in range(len(binary_n)):
			if binary_n[num] == "1":
				if last_index != -1:
					grap = max(grap, num - last_index)
				last_index = num
		return grap

n = 22
obj = Solution()
print(obj.binaryGap(n))