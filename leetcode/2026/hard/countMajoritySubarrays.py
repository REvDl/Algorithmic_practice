from typing import List





class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tree_size = 2*n
        tree = [0] * (tree_size * 2 + 2)
        def update(pos, val):
            pos += tree_size
            tree[pos] += val
            while pos > 1:
                tree[pos >> 1] = tree[pos] + tree[pos ^ 1]
                pos //=2
        def query(l, r):
            res = 0
            l += tree_size
            r += tree_size
            while l < r:
                if l & 1:
                    res += tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res += tree[r]
                l >>=1
                r >>=1
            return res
        res = 0
        update(n, 1)
        current_sum = 0
        for idx, num in enumerate(nums):
            current_sum += (1 if num == target else -1)
            res += query(0, current_sum + n)
            update(current_sum + n, 1)
        return res



obj = Solution()
nums = [1,2,2,3]
target = 2
print(obj.countMajoritySubarrays(nums, target))
            
