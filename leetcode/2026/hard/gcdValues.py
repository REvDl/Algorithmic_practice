from typing import List
from math import gcd
from collections import defaultdict, Counter
import bisect

class Solution:
    def gcdValues_v1(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        gcdPairs = []
        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                gcdPairs.append(gcd(nums[i], nums[j]))
        gcdPairs.sort()
        answer = []
        for query in queries:
            answer.append(gcdPairs[query])
        return answer

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        max_element = max(nums)
        count_nod = defaultdict(int)
        counts = Counter(nums)
        for g in range(max_element, 0, -1):
            total_m = 0
            for j in range(g, max_element + 1, g):
                total_m += counts[j]
            total_p = (total_m * (total_m - 1)) // 2
            for j in range(g * 2, max_element + 1, g):
                total_p -= count_nod[j]
            count_nod[g] = total_p
        prefix_sum = [0] * (max_element + 1)
        
        for i in range(1, max_element + 1):
            prefix_sum[i] = prefix_sum[i - 1] + count_nod[i]
        answer = []

        for query in queries:
            idx = bisect.bisect_right(prefix_sum, query)
            answer.append(idx)
        return answer
obj = Solution()
nums = [2,3,4]
queries = [0,2,2]
print(obj.gcdValues(nums, queries))
