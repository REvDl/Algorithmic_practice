from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        log_table = [0] * (n + 1)
        for i in range(2, n+1):
            log_table[i] = log_table[i // 2] + 1
        K_log = log_table[n] + 1
        
        st_max = [[0] * n for _ in range(K_log)]
        st_min = [[0] * n for _ in range(K_log)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        for j in range(1, K_log):
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))])
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + (1 << (j - 1))])

        def get_val(L, R):
            j = log_table[R - L + 1]
            max_val = max(st_max[j][L], st_max[j][R - (1 << j) + 1])
            min_val = min(st_min[j][L], st_min[j][R - (1 << j) + 1])
            return max_val - min_val
        heap = []
        for i in range(n):
            val = get_val(i, n-1)
            heapq.heappush(heap, (-val, i, n-1))
        total_value = 0
        for _ in range(k):
            if not heap:
                break
            neg_val, l, r = heapq.heappop(heap)
            total_value += (-neg_val)
            if r > l:
                next_val = get_val(l, r - 1)
                heapq.heappush(heap, (-next_val, l, r - 1))
        return total_value


obj = Solution()
nums = [11, 5]
k = 2
print(obj.maxTotalValue(nums, k))
