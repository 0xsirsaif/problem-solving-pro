"""
Problem:
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

notes and review:
- How the dummy node take a next node for only one time __ the first iteration?
That's because dummy and ptr are the same object before the new assignment of the ptr (ptr = XXX).
So, any modification (except an assignment) on the ptr will affect on the dummy node.

TODO
    TEST
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                print("12", dummy.next)
                ptr.next = l2
                l2 = l2.next
            else:
                ptr.next = l1
                l1 = l1.next
            ptr = ptr.next

        ptr.next = l1 or l2
        return dummy.next


C = ListNode(3, None)
B = ListNode(2, C)
A = ListNode(1, B)

Z = ListNode(4, None)
Y = ListNode(4, Z)
X = ListNode(4, Y)

S = Solution()
S.mergeTwoLists(A, X)
