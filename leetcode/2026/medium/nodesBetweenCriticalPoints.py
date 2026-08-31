from typing import List, Optional

class ListNode: 
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
        prev, curr, next = None, head, head
        curr_idx = 0
        while next and next.next:
            prev = curr
            curr = next
            curr_idx += 1
            next = next.next
            if prev.val > curr.val < next.val or prev.val < curr.val > next.val:
                res.append(curr_idx)
        n = len(res)
        if n < 2:
            return [-1, -1]
        res.sort()
        max_e = abs(res[-1] - res[0])
        min_e = float("inf")
        for i in range(1, n):
            min_e = min(min_e, abs(res[i] - res[i - 1]))
        return [min_e, max_e]




