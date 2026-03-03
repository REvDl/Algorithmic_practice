
class Solution:
    def reverse(self, x):
        return x[::-1]

    def invert(self, x):
        x_res = ""
        for i in x:
            if i == "1":
                x_res += "0"
            else:
                x_res += "1"
        return x_res

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        sn = "0"
        for i in range(1, n):
            sn = sn + "1" + self.reverse(self.invert(sn))
            if len(sn) > k:
                break
        return sn[k-1]

obj = Solution()
print(obj.findKthBit(4, 11))