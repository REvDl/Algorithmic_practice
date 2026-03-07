class Solution_1:
	def minFlips_1(self, s: str) -> int:
		n = len(s)
		s2 = s+s
		ans = n
		for start in range(n):
			count0 = 0
			count1 = 0
			for i in range(n):
				if s2[start + i] != ("0" if i % 2 == 0 else "1"):
					count0 += 1
				if s2[start + i] != ("1" if i % 2 == 0 else "0"):
					count1 += 1
			ans = min(count0, count1, ans)
		return ans




class Solution:
	def minFlips(self, s: str) -> int:
		n = len(s)
		s2 = s + s
		target1 = "01" * n
		target2 = "10" * n
		ans = float("inf")
		diff1 = 0
		diff2 = 0
		for i in range(2 * n):
			if s2[i] != target1[i]:
				diff1 += 1
			if s2[i] != target2[i]:
				diff2 += 1
			if i >= n:
				left_index = i - n
				if s[left_index] != target1[left_index]:
					diff1 -= 1
				if s[left_index] != target2[left_index]:
					diff2 -= 1
			if i >= n - 1:
				ans = min(ans, diff1, diff2)
		return ans




# count0 = 0
# n = len(s)
# for key, value in enumerate(s):
# 	if (key % 2 == 0 and value != "0") or (key % 2 != 0 and value != "1"):
# 		count0 += 1
# return min(n - count0, count0)


obj = Solution()
expected = ["111000", "010", "1110", "01001001101"]
for i in expected:
	print(obj.minFlips(i))

