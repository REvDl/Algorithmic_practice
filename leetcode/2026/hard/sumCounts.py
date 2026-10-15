


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self.build(data, 2 * v, tl, tm)
            self.build(data, 2 * v + 1, tm + 1, tr)

            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def update(self, v, tl, tr, idx, val):
        if tl == tr:
            self.tree[v] = val
        else:
            tm = (tl + tr) // 2
            if idx <= tm:
                self.update(2 * v, tl, tm, idx, val)
            else:
                self.update(2 * v + 1, tm + 1, tr, idx, val)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def query(self, v, tl, tr, l, r):
        if l > r: 
            return 0
        if l == tl and r == tr:
            return self.tree[v]
            
        tm = (tl + tr) // 2
        left_sum = self.query(2 * v, tl, tm, l, min(r, tm))
        right_sum = self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        return left_sum + right_sum



arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print(st.query(1, 0, st.n - 1, 1, 3)) 

