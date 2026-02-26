from typing import Optional


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		my_set = set()
		while head is not None:
			if head in my_set:
				return True
			my_set.add(head)
			head = head.next
		return False


class Solution_v2:
	def hasCycle_v2(self, head: Optional[ListNode]) -> bool:
		step = head
		next_step = head
		while next_step and next_step.next:
			next_step = next_step.next.next
			step = step.next
			if step == next_step:
				return True
		return False