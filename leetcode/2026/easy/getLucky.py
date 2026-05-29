


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        current_sum = 0
        for char in s:
            num = ord(char) - ord('a') + 1
            while num > 0:
                current_sum += num % 10
                num //=10
        for _ in range(k - 1):
            next_sum = 0
            while current_sum > 0:
                next_sum += current_sum % 10
                current_sum //=10
            current_sum = next_sum
        return current_sum









obj = Solution()
print(obj.getLucky("iiii", 1))
