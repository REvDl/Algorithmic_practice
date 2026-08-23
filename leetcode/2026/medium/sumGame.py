


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        left, right = num[:mid], num[mid:]
        sum_left = quetion_left = 0
        sum_right = quetion_right = 0
        for i, char in enumerate(num):
            if i < mid:
                if char == "?":
                    quetion_left += 1
                else:
                    sum_left += int(char)
            else:
                if char == "?":
                    quetion_right += 1
                else:
                    sum_right += int(char)
        diff_sum = sum_left - sum_right
        diff_quetion = quetion_left - quetion_right
        return False if diff_quetion % 2 == 0 and diff_sum * 2 + diff_quetion * 9 == 0 else True



obj = Solution()
num = "5023"
print(obj.sumGame(num))
