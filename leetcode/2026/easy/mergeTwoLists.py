from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoListsNonNode(self, list1: list[int], list2: list[int]) -> list[int]:
        n, m = len(list1), len(list2)
        if n != m:
            return "Sizes should not differ"
        merge_list = []
        for i in range(n):
            if list1[i] <= list2[i]:
                merge_list.append(list1[i])
        return merge_list


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        dummy = ListNode()
        tail = dummy
        while curr1 or curr2:
            if curr1 is None:
                tail.next = curr2
                break
            if curr2 is None:
                tail.next = curr1
                break
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        return dummy.next

obj = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(obj.mergeTwoListsNonNode(list1, list2))


