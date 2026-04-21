from typing import List
from collections import Counter, defaultdict


class Solution:
	def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
		n = len(source)
		parent = list(range(n))
		def find(i):
			if parent[i] == i:
				return i
			parent[i] = find(parent[i])
			return parent[i]
		def union(i, j):
			root_i = find(i)
			root_j = find(j)
			if root_i != root_j:
				parent[root_i] = root_j
		for a, b in allowedSwaps:
			union(a, b)

		count_source = defaultdict(Counter)
		count_target = defaultdict(Counter)
		min_dist = 0
		for i in range(n):
			index = find(i)
			count_source[index][source[i]] += 1
			count_target[index][target[i]] += 1
		for index in count_source:
			conn = count_target[index] & count_source[index]
			coincidences = sum(conn.values())
			min_dist += len(count_source[index].values()) - coincidences
		return min_dist


obj = Solution()
source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]
print(obj.minimumHammingDistance(source, target, allowedSwaps))
