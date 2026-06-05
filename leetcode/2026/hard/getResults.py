from typing import List
from bisect import bisect_right, bisect_left
import bisect


class SegmentTree:
    MAXX = 50000
    def __init__(self):
        self.tree = [0] * (4 * self.MAXX + 1)

    def update(self, curr_idx, l, r, idx, val):
        if l == r:
            self.tree[curr_idx] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(curr_idx * 2, l, mid, idx, val)
        else:
            self.update(curr_idx * 2 + 1, mid + 1, r, idx, val)
        self.tree[curr_idx] = max(self.tree[2 * curr_idx], self.tree[2 * curr_idx + 1])

    def query(self, curr_idx, l, r, ql, qr):
        if r < ql or l > qr:
            return 0
        if ql <= l and qr <= r:
            return self.tree[curr_idx]
        mid = (l + r) // 2
        left_res = self.query(2 * curr_idx, l, mid, ql, qr)
        right_res = self.query(2 * curr_idx + 1, mid + 1, r, ql, qr)
        return max(left_res, right_res)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sorted_set = SortedSet([0])
        segment = SegmentTree()
        for query in queries:
            if query[0] == 1:
                sorted_set.add(query[1])
        positions = list(sorted_set)
        for i in range(1, len(positions)):
            segment.update(1, 0, segment.MAXX, positions[i], positions[i] - positions[i - 1])

        ans = []

        for i in range(len(queries) -1, -1, -1):
            if queries[i][0] == 2:
                x = queries[i][1]
                idx = sorted_set.bisect_right(x) - 1
                left_obst = sorted_set[idx]
                res_tree = segment.query(1, 0, segment.MAXX, 0, left_obst)
                tail = x - left_obst
                if max(tail, res_tree) >= queries[i][2]:
                    ans.append(True)
                else:
                    ans.append(False)
            else:
                x = queries[i][1]
                idx = sorted_set.index(x)
                left_pos = sorted_set[idx - 1]
                segment.update(1, 0, segment.MAXX, x, 0)
                if idx + 1 < len(sorted_set):
                    right_pos = sorted_set[idx + 1]
                    segment.update(1, 0, segment.MAXX, right_pos, right_pos - left_pos)
                sorted_set.remove(x)
        return ans[::-1]



obj = Solution()
print(obj.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
