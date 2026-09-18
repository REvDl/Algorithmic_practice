from collections import Counter
from itertools import islice

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        indexes = {}
        for index, char in enumerate(s):
            if char not in indexes:
                indexes[char] = (index, index)
            else:
                indexes[char] = (indexes[char][0], index)

        indexes_substrings = []
        for start, end in indexes.values():
            curr = start
            while curr <= end:
                char = s[curr]
                if indexes[char][1] > end:
                    end = indexes[char][1]

                if indexes[char][0] < start:
                    start = indexes[char][0]
                    curr = start
                curr += 1
            indexes_substrings.append((start,end))

        sorted_indexes = sorted(indexes_substrings, key=lambda x: x[1])
        res = [(sorted_indexes[0][0], sorted_indexes[0][1])]


        for start, end in islice(sorted_indexes, 1, None):
            if start > res[-1][1]:
                res.append((start, end))
            else:
                continue
        return [s[start:end+1] for start, end in res]

obj = Solution()
s = "dzdabazbbccd"
print(obj.maxNumOfSubstrings(s))
