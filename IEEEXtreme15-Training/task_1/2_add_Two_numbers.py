"""
Problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Review and Notes:

TODO
    REVIEW
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # brute-force solution = sucks
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next

        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        result = str(int(''.join(str(n) for n in list1)[::-1]) + int(''.join(str(n) for n in list2)[::-1]))
        print(result)
        dummy = curr = ListNode(0)
        for i in str(result[::-1]):
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                sum = l2.val + carry
                l2 = l2.next
            else:
                sum = l1.val + carry
                l1 = l1.next

            val, carry = (sum % 10), (sum // 10)
            curr.next = ListNode(val)
            curr = curr.next

        if carry:
            curr.next = ListNode(1)
        return dummy.next


C = ListNode(9, None)
B = ListNode(4, C)
A = ListNode(2, B)

V = ListNode(9, None)
Z = ListNode(4, V)
Y = ListNode(6, Z)
X = ListNode(5, Y)

S = Solution()
S.addTwoNumbers(A, X)