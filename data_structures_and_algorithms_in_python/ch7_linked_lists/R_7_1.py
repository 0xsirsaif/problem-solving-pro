"""
Problem:
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.

Algorithm description:
Moving the ptr from the head to the outer of the list (None = tail.next), and only move the prev if ptr is not None

Notes and review:
- Dummy Node always come in handy
- while ptr >> while ptr.next
- think after ptr.next! Do tou need conditions?
- explicit return always win, return prev.element >> return prev.next.element, or so
- single return >> double return
"""
from data_structures_implementation import SinglyLinkedList, DummyNode
import unittest


def find_second_to_last(head):
    ptr = head
    prev = DummyNode(None, head)
    while ptr:
        ptr = ptr.next
        if ptr:
            prev = prev.next
    return prev.element


class TestFindSecondToLast(unittest.TestCase):
    def test_find_second_to_last_empty_list(self):
        # [] -> the result is None
        s = SinglyLinkedList()
        actual = find_second_to_last(s.head)
        expected = None
        self.assertEqual(actual, expected)

    def test_find_second_to_last_one_element(self):
        # [1] -> the result is None
        s = SinglyLinkedList()
        s.add_first(1)
        actual = find_second_to_last(s.head)
        expected = None
        self.assertEqual(actual, expected)

    def test_find_second_to_last_two_elements(self):
        # [1, 2] -> the result is 1
        s = SinglyLinkedList()
        s.add_first(2)
        s.add_first(1)
        actual = find_second_to_last(s.head)
        expected = 1
        self.assertEqual(actual, expected)

    def test_find_second_to_last_multi_elements(self):
        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] -> the result is 1
        s = SinglyLinkedList()
        for i in range(10):
            s.add_first(i)
        actual = find_second_to_last(s.head)
        expected = 1
        self.assertEqual(actual, expected)
