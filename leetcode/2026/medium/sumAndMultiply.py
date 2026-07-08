from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        n = len(s)
        prefix_sum = [0] * (n + 1)
        digits = [int(num) for num in s]
        pref_val = [0] * (n + 1)
        pref_len = [0] * (n + 1)
        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i-1] * 10) % MOD
        for i in range(n):
            x = digits[i]
            prefix_sum[i+1] = prefix_sum[i] + x
            if x != 0:
                pref_val[i+1] = (pref_val[i] * 10 + x) % MOD
                pref_len[i+1] = pref_len[i] + 1
            else:
                pref_val[i+1] = pref_val[i]
                pref_len[i+1] = pref_len[i]
        ans = []
        for l, r in queries:
            k = pref_len[r + 1] - pref_len[l]
            x_val = (pref_val[r+1] - pref_val[l] * powers[k]) % MOD
            sum_range = (prefix_sum[r+1] - prefix_sum[l]) % MOD
            ans.append((x_val * sum_range) % MOD)
        return ans


obj = Solution()
s = "10203004"
queries = [[0,7],[1,3],[4,6]]
print(obj.sumAndMultiply(s, queries))
