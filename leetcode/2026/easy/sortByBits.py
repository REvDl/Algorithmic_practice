from itertools import count


class Solution:
	def sortByBits(self, arr:list[int]):
		arr.sort(key=lambda x: (x.bit_count(), x))
		return arr


obj = Solution()
print(obj.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))