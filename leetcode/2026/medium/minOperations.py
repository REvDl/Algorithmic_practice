from collections import defaultdict



class Solution:
    def minOperations(self, s: str) -> int:
        sort_s = "".join(sorted(s))
        n = len(s)
        if s == sort_s:
            return 0
        if n <= 2:
            return -1
        chars = defaultdict(list)
        lvl = 0
        last_idx = 0
        for i in range(1, n - 1):
            curr, next = s[i-1], s[i]
            if i - last_idx > 1:
                lvl += 1
            if curr > next:
                chars[lvl].append(curr)
                last_idx = i - 1
        if (n - 1) - last_idx > 1:
            lvl += 1
        if s[-2] > s[-1]:
            chars[lvl].append(s[-2])
        res = len(chars)
        if res == 1:
            return 1
        elif res == 2:
            return 2
        else:
            return 3

s2 = "cbarcba"
obj = Solution()
print(obj.minOperations(s2))
s = ["dog", "card"]
for chr in s:
    print(obj.minOperations(chr))
