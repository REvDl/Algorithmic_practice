from typing import List
from collections import namedtuple



class Solution_1:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:        
        def maxActiveSectiionsAfterQuery(s: str, orig_s: str) -> int:
            t = '1' + s + '1'
            length_array = []
            length = 1
            for i in range(1, len(t)):
                if t[i-1] == t[i]:
                    length += 1
                else:
                    length_array.append((t[i-1], length))
                    length = 1
            max_gain = 0
            for i in range(1, len(length_array) - 1):
                prev_char, prev_length = length_array[i-1]
                curr_char, curr_lenght = length_array[i]
                next_char, next_length = length_array[i+1]
                if curr_char == '1' and prev_char == '0' and next_char == '0':
                    max_gain = max(max_gain, prev_length + next_length)
            return orig_s.count('1') + max_gain
        ans = []
        for query in queries:
            gain = maxActiveSectiionsAfterQuery(s[query[0]:query[1] + 1], s)
            res = s[:query[0]].count('1') + gain + s[query[1]:].count('1')
            ans.append(gain)
        return ans



    






class Solution_2:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        i = 0
        length_array = []
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                end = i - 1
                length = end - start + 1
                length_array.append((start, end, length))
            else:
                i += 1
        Node = namedtuple('Node', ['size', 'total', 'prefix', 'suffix'])
        memo = {}
        def merge(left, right):
            merged = left.suffix +right.prefix
            size = left.size + right.size
            total = max(left.total, right.total, merged)
            prefix = left.prefix + right.prefix if left.total == left.size else left.prefix
            suffix = right.suffix + left.suffix if right.total == right.size else right.suffix
            return Node(size=size, total=total, prefix=prefix, suffix=suffix)


        def build(left, right):
            if left == right:
                is_zero = 1 if s[left] == '0' else 0
                node = Node(size=right - left + 1,total=is_zero, prefix=is_zero, suffix=is_zero)
                memo[(left, right)] = node
                return node
            mid = (left + right) // 2
            left_node = build(left, mid)
            right_node = build(mid + 1, right)
            merge_node = merge(left_node, right_node)
            memo[(left, right)] = merge_node
            return merge_node


        def query(nodeL, nodeR, left, right):
            if right < nodeL or nodeR < left:
                return Node(size=0, total=0, prefix=0, suffix=0)
            if left <= nodeL and nodeR <= right:
                return memo[(nodeL, nodeR)]
            mid = (nodeL + nodeR) // 2
            left_result = query(nodeL, mid, left, right)
            right_result = query(mid + 1, nodeR, left, right)
            return merge(left_result, right_result)
        build(0, n-1)
        ans = []
        for query in queries:
            total = query(0, n-1, query[0], query[1])
        #This doesn't work, I decided to keep it as a memory because it took me 4 hours.




class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(data, 1, 0, self.n - 1)
            
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self.build(data, 2 * node, start, mid)
        self.build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
        
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r),
                   self.query(2 * node + 1, mid + 1, end, l, r))

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones_s = s.count('1')
        blocks = []
        i = 0
        while i < n:
            start = i
            char = s[i]
            while i < n and s[i] == char:
                i += 1
            end = i - 1
            blocks.append((char, start, end, end - start + 1))
        num_blocks = len(blocks)
        block_idx = [-1] * n
        for idx, (b_type, start, end, _) in enumerate(blocks):
            for k in range(start, end + 1):
                block_idx[k] = idx
        internal_gain = [0] * num_blocks
        for idx in range(num_blocks):
            b_type, start, end, length = blocks[idx]
            if b_type == '1' and idx > 0 and idx < num_blocks - 1:
                left_0_start = blocks[idx-1][1]
                right_0_end = blocks[idx+1][2]
                internal_gain[idx] = (start - left_0_start) + (right_0_end - end)
        tree = SegmentTree(internal_gain)
        ans = []
        for L, R in queries:
            bl = block_idx[L]
            br = block_idx[R]
            max_gain = 0
            candidates = set()
            for idx in (bl, bl + 1, br - 1, br):
                if 0 <= idx < num_blocks:
                    candidates.add(idx)
            for idx in candidates:
                b_type, start, end, length = blocks[idx]
                if b_type == '1' and start >= L + 1 and end <= R - 1:
                    left_0_start = blocks[idx-1][1]
                    right_0_end = blocks[idx+1][2]
                    
                    g_left = start - max(L, left_0_start)
                    g_right = min(R, right_0_end) - end
                    
                    if g_left + g_right > max_gain:
                        max_gain = g_left + g_right
            if bl + 2 <= br - 2:
                tree_max = tree.query(1, 0, tree.n - 1, bl + 2, br - 2)
                if tree_max > max_gain:
                    max_gain = tree_max
                    
            ans.append(total_ones_s + max_gain)
            
        return ans


obj = Solution()
s = "0100"
queries = [[1,5],[0,6],[0,4]]
print(obj.maxActiveSectionsAfterTrade(s, queries))
