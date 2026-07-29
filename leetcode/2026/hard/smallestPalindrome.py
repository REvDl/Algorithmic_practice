
class Solution:
    #it didn't work
    def smallestPalindrome(self, s: str, k: int) -> str:
        count_letter = Counter(s)
        n = len(s)
        h = n // 2
        fact = [1] * (h + 1)
        for i in range(1, h + 1):
            fact[i] = fact[i - 1] * i
        mid = ''
        half_counts = {}
        for chr, cnt in count_letter.items():
            if cnt % 2 == 1:
                mid = chr
            if cnt // 2 > 0:
                half_counts[chr] = cnt // 2
        denom = 1
        for letter in half_counts:
            denom *= fact[half_counts[letter]]
        total_perms = fact[h] // denom
        if k > total_perms:
            return ""
        result = []
        remaining = h
        for i in range(h):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter in half_counts and half_counts[letter] > 0:
                    trial_denom = denom // fact[half_counts[letter]]
                    if trial_denom <= 0:
                        continue
                    perms = fact[remaining - 1] // trial_denom
                
                    if k <= perms:
                        result.append(letter)
                        denom = trial_denom
                        half_counts[letter] -= 1
                        remaining -= 1
                        break
                    else:
                        k -= perms
        return "".join(result)
        


obj = Solution()
s = "abba"
k = 2
print(obj.smallestPalindrome(s, k))
