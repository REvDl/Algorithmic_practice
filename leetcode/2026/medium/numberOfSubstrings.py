


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        idx_a, idx_b, idx_c = [], [], []
        for idx, char in enumerate(s):
            if char == "a": idx_a.append(idx)
            if char == "b": idx_b.append(idx)
            if char == "c": idx_c.append(idx)
        len_a, len_b, len_c = len(idx_a), len(idx_b), len(idx_c)
        for i in range(n):
            if idx_a and idx_a[0] < i:
                idx_a.pop(0)
            if idx_b and idx_b[0] < i:
                idx_b.pop(0)
            if idx_c and idx_c[0] < i:
                idx_c.pop(0)
        
            a = idx_a[0] if idx_a else -1
            b = idx_b[0] if idx_b else -1
            c = idx_c[0] if idx_c else -1 
            if a == -1 or b == -1 or c == -1:
                break
        
            max_idx = max(a, b, c)
            res += n - max_idx
        return res


class Solution_2:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        idx_a, idx_b, idx_c = [], [], []
        
        for idx, char in enumerate(s):
            if char == "a": idx_a.append(idx)
            if char == "b": idx_b.append(idx)
            if char == "c": idx_c.append(idx)
            
        len_a, len_b, len_c = len(idx_a), len(idx_b), len(idx_c)
        p_a, p_b, p_c = 0, 0, 0
        
        for i in range(n):
            while p_a < len_a and idx_a[p_a] < i:
                p_a += 1
            while p_b < len_b and idx_b[p_b] < i:
                p_b += 1
            while p_c < len_c and idx_c[p_c] < i:
                p_c += 1
            if p_a == len_a or p_b == len_b or p_c == len_c:
                break
        
            max_idx = max(idx_a[p_a], idx_b[p_b], idx_c[p_c])
            res += n - max_idx
        return res



obj = Solution()
s = "abcabc"
print(obj.numberOfSubstrings(s))
