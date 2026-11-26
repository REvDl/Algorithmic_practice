


class Solution:
    def canAliceWin(self, n: int) -> bool:
        bob_n = 10
        alice_n = 10
        whose_move = 0
        while True:
            if whose_move % 2 == 0:
                if alice_n > n:
                    return False
                elif alice_n == n:
                    return True
                whose_move += 1
                n -= alice_n
                bob_n = alice_n - 1
            else:
                if bob_n > n:
                    return True
                elif bob_n == n:
                    return False
                whose_move += 1
                n -= bob_n
                alice_n = bob_n - 1

obj = Solution()
n = 34
print(obj.canAliceWin(n))
