


class SegmentTree:
    def __init__(self, n: int, euler: list[str]):
        self.n = len(euler)
        self.arr = [0] * (self.n * 4 + 1)
        self.euler = euler
        if n > 0:
            self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.arr[node] = 1 << (ord(self.euler[l]) - ord('a'))
        elif l < r:
            mid = (l + r) // 2
            self.build(2 * node, l, mid)
            self.build(2 * node + 1, mid + 1, r)
            self.arr[node] = self.arr[2 * node] ^ self.arr[2 * node + 1]

        
    def update(self, idx, val):
        self.euler[idx] = val
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, l, r, idx, val):
        if l == r:
            self.arr[node] = 1 << (ord(val) - ord('a'))
            return
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(2 * node, l, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, r, idx, val)
        self.arr[node] = self.arr[2 * node] ^ self.arr[2 * node + 1]


    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, tl, tr, l, r):
        if r < tl or tr < l:
            return 0
        elif l <= tl and tr <= r:
            return self.arr[node]
        mid = (tl + tr) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        p1 = self._query(left_child, tl, mid, l, r)
        p2 = self._query(right_child, mid + 1, tr, l, r)
        return p1 ^ p2



class Solution:

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        euler = []
        first_pos = [-1] * n
        last_pos = [-1] * n
        def dfs(node, parent):
            first_pos[node] = len(euler)
            euler.append(s[node])
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            last_pos[node] = len(euler)
            euler.append(s[node])
        dfs(0, -1)
        answer = []
        segment = SegmentTree(n * 2, euler)
        for query in queries:
            if query[0] == "q":
                _, u_str, v_str = query.split()
                u, v = int(u_str), int(v_str)
                mask = segment.query(min(first_pos[u], first_pos[v]), max(first_pos[u], first_pos[v]))
                if mask == 0 or (mask & (mask - 1)) == 0:
                    answer.append(True)
                else:
                    answer.append(False)
            elif query[0] == "u":
                _, idx_str, chr = query.split()
                idx = int(idx_str)
                segment.update(first_pos[idx], chr)
                segment.update(last_pos[idx], chr)
        return answer


obj = Solution()
n = 4
edges = [[0,1],[0,2],[0,3]]
s = "abca"
queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
print(obj.palindromePath(n, edges, s, queries))
