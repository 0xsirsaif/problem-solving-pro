"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

TODO
    COMPLETE
    REVIEW
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # sucks
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def _reverse_group(start, to):
            prv = None
            curr = start
            if curr == to:
                return curr
            while curr:
                nxt = curr.next
                curr.next = prv
                prv = curr
                curr = nxt

            return start

        count = 0
        ptr = end = head
        while ptr:
            count += 1
            if count % k == 0:
                end = ptr
            ptr = ptr.next

        temp = end.next
        last = _reverse_group(head, end)
        last.next = temp

        return ptr
