



class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (self.n * 4)
        self.lazy = [0] * (self.n * 4)
        self.square = [0] * (self.n * 4)


    def push(self, v, tl, tr):
        if self.lazy[v] == 0:
            return
        tm = (tl + tr) // 2
        self.update(2 * v, tl, tm, tl, tm, self.lazy[v])
        self.update(2 * v + 1, tm + 1, tr, tm + 1, tr, self.lazy[v])
        self.lazy[v] = 0


    def update(self, v, tl, tr, l, r, val):
        if tl > r or tr < l:
            return
        elif l <= tl and tr <= r:
            length = tr - tl + 1
            self.square[v] = self.square[v] + 2 * val * self.tree[v] +  val * val * length
            self.tree[v] += val * length
            self.lazy[v] += val
            return 
        else:

            self.push(v, tl, tr)
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, r, val)
            self.update(2 * v + 1, tm + 1, tr, l, r, val)
            self.tree[v] =  self.tree[v * 2] + self.tree[v * 2 + 1]
            self.square[v] = self.square[v * 2] + self.square[v * 2 + 1]



class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        n = len(nums)
        tree = SegmentTree(nums)
        last_pos = {}
        for i in range(n):
            num = nums[i]
            if num in last_pos:
                left = last_pos[num] + 1
            else:
                left = 0
            tree.update(1, 0, n - 1, left, i, 1)
            res = (res + tree.square[1]) % MOD
            last_pos[num] = i
        return res



obj = Solution()
nums = [1,2,1]
print(obj.sumCounts(nums))
