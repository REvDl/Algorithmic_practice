from collections import Counter
from typing import List


class Solution:
	def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
		result = []
		for query in queries:
			for word in dictionary:
				diff = 0
				for k in range(len(word)):
					if query[k] != word[k]: diff += 1
					if diff > 2: break
				if diff <= 2:
					result.append(query)
					break
		return result


# note, joke, len = 4, note может стать joke, если len note >= len joke - 2??????????
obj = Solution()
queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
print(obj.twoEditWords(queries, dictionary))
