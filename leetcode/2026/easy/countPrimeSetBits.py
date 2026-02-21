class Solution(object):
	def countPrimeSetBits(self, left, right):
		counter = 0
		for n in range(left, right + 1):
			bit_n = bin(n)[2:]
			count_units = int(bit_n.count("1"))
			if count_units < 2:
				continue
			is_prime = True
			for i in range(2, count_units):
				if count_units % i == 0:
					is_prime = False
					break
			if is_prime:
				counter += 1
		return counter




obj = Solution()
print(obj.countPrimeSetBits(6, 10))


def twoSum(nums, target):
	result = dict()
	for i, num in enumerate(nums):
		x = target - num
		if x in result:
			return [result[x], i]
		else:
			result[num] = i
	return None

nums = [2, 8, 5, 5]
print(twoSum(nums, 10))
