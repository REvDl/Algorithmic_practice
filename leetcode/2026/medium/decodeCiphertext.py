class Solution:
	def decodeCiphertext(self, encodedText: str, rows: int) -> str:
		cols = len(encodedText) // rows
		res = []
		for i in range(cols):
			curr = i
			while curr < len(encodedText):
				res.append(encodedText[curr])
				curr += (cols + 1)
		return "".join(res).rstrip()







obj = Solution()
encodedText = "A d b  ae c "
rows = 3
print(obj.decodeCiphertext(encodedText, rows))