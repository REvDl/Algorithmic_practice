


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

    def add(self, idx, delta):
        self._add(1, 0, self.n - 1, idx, delta)

    def _add(self, node, l, r, idx, delta):
        if l == r:
            self.arr[node] ^= delta
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._add(2 * node, l, mid, idx, delta)
        else:
            self._add(2 * node + 1, mid + 1, r, idx, delta)
        self.arr[node] = self.arr[2 * node] ^ self.arr[2 * node + 1]


import math

class LCA:
    def __init__(self, n, adj, s, root=0):
        self.LOG = int(math.log2(n)) + 1
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.tin = [0] * n
        self.tout = [0] * n
        self.timer = 0
        self.euler_nodes = []
        self.base = [0] * n
        self.s = s
        self.dfs(root, root, adj)

    def dfs(self, v, p, adj):
        self.tin[v] = self.timer
        self.timer += 1
        self.euler_nodes.append(v)
        self.base[v] = (self.base[p] if v != p else 0) ^ (1 << (ord(self.s[v]) - ord('a')))
        self.up[v][0] = p
        for i in range(1, self.LOG):
            if self.up[v][i-1] != -1:
                self.up[v][i] = self.up[self.up[v][i-1]][i-1]
                
        for to in adj[v]:
            if to != p:
                self.dfs(to, v, adj)
                
        self.tout[v] = self.timer
        self.timer += 1

    def is_ancestor(self, u, v):
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def get_lca(self, u, v):
        if self.is_ancestor(u, v):
            return u
        if self.is_ancestor(v, u):
            return v
        for i in range(self.LOG - 1, -1, -1):
            if self.up[u][i] != -1 and not self.is_ancestor(self.up[u][i], v):
                u = self.up[u][i]
        return self.up[u][0]




class Solution:

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lca = LCA(n, adj, s, 0)
        segment = SegmentTree(2 * n + 2, ["a"] * (2 * n + 2))
        segment.arr = [0] * len(segment.arr)
        answer = []
        for query in queries:
            parts = query.split()
            if parts[0][0] == "q":
                u, v = int(parts[1]), int(parts[2])
                w = lca.get_lca(u, v)
                val_u = lca.base[u] ^ segment.query(0, lca.tin[u])
                val_v = lca.base[v] ^ segment.query(0, lca.tin[v])
                mask = val_u ^ val_v ^ (1 << (ord(s[w]) - 97))
                if mask == 0 or (mask & (mask - 1)) == 0:
                    answer.append(True)
                else:
                    answer.append(False)
            elif parts[0][0] == "u":
                idx = int(parts[1])
                chr_val = parts[2]
                delta = (1 << (ord(s[idx]) - 97)) ^ (1 << (ord(chr_val) - 97))
                segment.add(lca.tin[idx], delta)
                segment.add(lca.tout[idx] + 1, delta)
                s = s[:idx] + chr_val + s[idx + 1:]
        return answer





obj = Solution()
n = 4
edges = [[0,1],[0,2],[0,3]]
s = "abca"
queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
print(obj.palindromePath(n, edges, s, queries))
