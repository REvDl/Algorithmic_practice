

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        def replaceConsecutive(s: str, k: int, n: int) -> str:
            if n <= k:
                return s
            consecutive_groups = []
            count, curr_sum = 0, 0
            for idx, num in enumerate(s):
                count += 1
                curr_sum += int(num)
                if count == k or idx == (n - 1):
                    consecutive_groups.append(str(curr_sum))
                    curr_sum = 0
                    count = 0
            return "".join(consecutive_groups)
        res = replaceConsecutive(s, k, n)
        m = len(res)
        while m > k:
            res = replaceConsecutive(res, k, m)
            m = len(res)
        return res



obj = Solution()
s = "11111222223"
k = 3
print(obj.digitSum(s, k))
