from typing import List
from collections import deque


class Solution:
	def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
		n = len(online)
		graph = [[] for _ in range(n)]
		for u, v, cost in edges:
			graph[u].append((v, cost))
		in_degree = [0] * n
		for u, v, _ in edges:
			in_degree[v] += 1

		q = deque([i for i in range(n) if in_degree[i] == 0])
		topo_order = []
		while q:
			curr = q.popleft()
			topo_order.append(curr)
			for neighbor, _ in graph[curr]:
				in_degree[neighbor] -= 1
				if in_degree[neighbor] == 0:
					q.append(neighbor)
		def check(min_allowed_edge) -> bool:
			dp = [float('inf')] * n
			dp[0] = 0
			for curr in topo_order:
				if dp[curr] == float('inf'):
					continue

				for neighbor, cost in graph[curr]:
					if not online[neighbor] or cost < min_allowed_edge:
						continue

					new_cost = dp[curr] + cost
					if new_cost <= k and new_cost < dp[neighbor]:
						dp[neighbor] = new_cost

			return dp[n - 1] <= k

		left = 0
		all_costs = sorted(list(set(cost for _, _, cost in edges)))
		if not all_costs:
			return -1
		right = len(all_costs) - 1
		ans = -1
		while left <= right:
			mid = (left + right) // 2
			mid_cost = all_costs[mid]
			if check(mid_cost):
				ans = mid_cost
				left = mid + 1
			else:
				right = mid - 1

		return ans




obj = Solution()
edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]]
online = [True,True,True,False, True]
k = 12
print(obj.findMaxPathScore(edges, online, k))