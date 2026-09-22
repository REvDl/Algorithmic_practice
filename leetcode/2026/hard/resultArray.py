from typing import List


class SegmentTree:
    def __init__(self, data, k):
        self.n = len(data)
        self.data = data
        self.k = k
        self.tree = [self._neutral_element()] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _neutral_element(self):
        return (1, [0] * self.k)

    def _merge(self, left_child, right_child):
        left_prod, left_rem = left_child
        right_prod, right_rem = right_child
        parent_prod = (left_prod * right_prod) % self.k
        parent_rem = [0] * self.k
        for x in range(self.k):
            parent_rem[x] += left_rem[x]
            
        for j in range(self.k):
            new_rem = (left_prod * j) % self.k
            parent_rem[new_rem] += right_rem[j]
            
        return (parent_prod, parent_rem)

    def _build(self, node, start, end):
        if start == end:
            val = self.data[start] % self.k
            rem = [0] * self.k
            rem[val] = 1
            self.tree[node] = (val, rem)
            return
        
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            val = val % self.k
            rem = [0] * self.k
            rem[val] = 1
            self.tree[node] = (val, rem)
            return
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
            
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return self._neutral_element()
        
        if l <= start and end <= r:
            return self.tree[node]
            
        mid = (start + end) // 2
        left_res = self._query(2 * node, start, mid, l, r)
        right_res = self._query(2 * node + 1, mid + 1, end, l, r)
        
        return self._merge(left_res, right_res)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        node = SegmentTree(nums, k)
        for query in queries:
            idx, val, start, x = query
            node.update(idx, val)
            res = node.query(start, n - 1)
            ans.append(res[1][x])
        return ans


obj = Solution()
nums = [1,2,3,4,5]
k = 3
queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
print(obj.resultArray(nums, k, queries))

