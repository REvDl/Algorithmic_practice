from collections import Counter



class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        n = len(word)
        frequency = sorted(Counter(word).values(), reverse=True)
        for i in range(len(frequency)):
            pushes += (i // 8 + 1) * frequency[i]
        return pushes


obj = Solution()
word = "xyzxyzxyzxxyyyyyyyyyyzzzz"
print(obj.minimumPushes(word))
