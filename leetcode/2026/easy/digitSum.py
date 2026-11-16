

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            curr_sum = 0
            consecutive_groups = []
            for count, char in enumerate(s, 1):
                curr_sum += int(char)
                if count % k == 0 or count == n:
                    consecutive_groups.append(str(curr_sum))
                    curr_sum = 0
            s = "".join(consecutive_groups)
            n = len(s)
        return s



obj = Solution()
s = "11111222223"
k = 3
print(obj.digitSum(s, k))
