# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution(object):
	def list_to_listnode(self, lst):
		dummy = current = ListNode(0)
		for val in lst:
			current.next = ListNode(val)
			current = current.next
		return dummy.next

	def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]):
		node = l1
		node_two = l2
		result = []
		result_two = []
		while node or node_two:
			val1 = node.val if node and node else 0
			val2 = node_two.val if node_two else 0
			result.append(val1)
			result_two.append(val2)
			node = node.next if node else None
			node_two = node_two.next if node_two else None
		result_finally = [int(x) for x in str((int(("".join(str(x) for x in result))[::-1]) + int(("".join(str(x) for x in result_two))[::-1])))][::-1]
		return Solution.list_to_listnode(self, result_finally)

obj = Solution()
nums = ListNode(2, ListNode(4, ListNode(3)))
nums_two = ListNode(5, ListNode(6, ListNode(4)))
print(obj.addTwoNumbers(nums, nums_two))


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		dummy = current = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0
			total = v1 + v2 + carry
			carry = total // 10
			current.next = ListNode(total % 10)
			current = current.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
		return dummy.next