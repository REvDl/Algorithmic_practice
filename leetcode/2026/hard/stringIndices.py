from typing import List


class TrieNode:
    def __init__(self, best_index = -1):
        self.node = {}
        self.best_index = best_index

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        best_index = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best_index]):
                best_index = i
        node = TrieNode(best_index)
        for idx, word in enumerate(wordsContainer):
            curr = node
            word_reverse = word[::-1]
            for letter in word_reverse:
                if letter not in curr.node:
                    curr.node[letter] = TrieNode(idx)
                curr = curr.node[letter]
                if len(wordsContainer[idx]) < len(wordsContainer[curr.best_index]):
                    curr.best_index = idx
        ans = []
        for idx, word in enumerate(wordsQuery):
            curr = node
            word_reverse = word[::-1]
            for letter in word_reverse:
                if letter in curr.node:
                    curr = curr.node[letter]
                else:
                    break
            ans.append(curr.best_index)
        return ans












obj = Solution()
wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
print(obj.stringIndices(wordsContainer, wordsQuery))
