from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # bad
    def badmiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        ptr = head
        while ptr:
            size += 1
            ptr = ptr.next

        middle_idx = size // 2
        ptr2 = head
        idx = 0
        while ptr2:
            idx += 1
            if idx == middle_idx:
                return ptr2
            ptr2 = ptr2.next
            idx += 1

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        So when the `fast` reaches the end of the list, the `slow` just reaches the half of it.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow