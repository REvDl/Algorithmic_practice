from typing import List



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        vector = []
        twin_sum = 0
        while curr:
            vector.append(curr.val)
            curr = curr.next
        n = len(vector)
        for i in range(n // 2):
            twin_sum = max(vector[i] + vector[n - 1 - i], twin_sum)
        return twin_sum 

