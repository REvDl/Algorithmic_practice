class Solution:
	def isPalindrome(self, x: int) -> bool:
		reversed_number = 0
		n = x
		if x < 0:
			return False
		while n > 0:
			last_number = n % 10
			reversed_number = (reversed_number * 10) + last_number
			n = n // 10
		if reversed_number == x:
			return True
		return False


obj = Solution()
print(obj.isPalindrome(-123))