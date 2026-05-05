
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
	def rotateRight_dirty_version(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if not head or k == 0: return head
		curr = head
		len_head = 1
		while curr.next:
			len_head += 1
			curr = curr.next
		k = k % len_head
		if k == 0:
			return head
		curr.next = head
		slice = len_head - k
		i = 1
		node = head
		start_node = None
		while node.next:
			if i == slice:
				start_node = node.next
				node.next = None
				break
			i += 1
			node = node.next
		return start_node

	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if not head or k == 0: return head
		curr, len_head = head, 1
		while curr.next:
			len_head += 1
			curr = curr.next
		k %= len_head
		if k == 0: return head
		curr.next = head
		node = head
		split_index = len_head - k
		for _ in range(split_index - 1):
			node = node.next
		start_node = node.next
		node.next = None
		return start_node

obj = Solution()
head = [1,2,3,4,5]
k = 2
print(obj.rotateRight(head, k))