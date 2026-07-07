

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_num = bin(n)[2:]
        res = 0
        for num in bit_num:
            res += int(num)
        return res
        



obj = Solution()
print(obj.hammingWeight(11))
