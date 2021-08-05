"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
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
        s = SinglyLinkedList()
        actual = find_second_to_last(s.head)
        expected = None
        self.assertEqual(actual, expected)

    def test_find_second_to_last_one_element(self):
        s = SinglyLinkedList()
        s.add_first(10)
        actual = find_second_to_last(s.head)
        expected = None
        self.assertEqual(actual, expected)

    def test_find_second_to_last_two_elements(self):
        s = SinglyLinkedList()
        s.add_first(10)
        actual = find_second_to_last(s.head)
        expected = None
        self.assertEqual(actual, expected)

    def test_find_second_to_last_multi_elements(self):
        s = SinglyLinkedList()
        for i in range(10):
            s.add_first(i)
        actual = find_second_to_last(s.head)
        expected = 1
        self.assertEqual(actual, expected)
