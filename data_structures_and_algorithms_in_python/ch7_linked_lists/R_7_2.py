"""
Problem:
Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L2
that contains all the nodes of L followed by all the nodes of M.

# TODO
    # REVIEW
"""
from data_structures_implementation.linked_lists import SinglyLinkedList
import unittest


def concatenate_lists(l, m):
    l2 = []
    while l:
        l2.append(l.element)
        l = l.next

    while m:
        l2.append(m.element)
        m = m.next

    return l2


class TestConcatenateLists(unittest.TestCase):
    def test_concatenate_lists_no_l_head(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        m.add_first(10)
        m.add_first(20)
        m.add_first(30)
        actual = concatenate_lists(l.head, m.head)
        expected = [30, 20, 10]
        self.assertEqual(actual, expected)

    def test_concatenate_lists_no_m_head(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        l.add_first(10)
        l.add_first(20)
        l.add_first(30)
        actual = concatenate_lists(l.head, m.head)
        expected = [30, 20, 10]
        self.assertEqual(actual, expected)

    def test_concatenate_lists_no_heads(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        actual = concatenate_lists(l.head, m.head)
        expected = []
        self.assertEqual(actual, expected)

    def test_concatenate_lists_one_element_in_l(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        l.add_first(10)
        actual = concatenate_lists(l.head, m.head)
        expected = [10]
        self.assertEqual(actual, expected)

    def test_concatenate_lists_one_element_in_m(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        m.add_first(10)
        actual = concatenate_lists(l.head, m.head)
        expected = [10]
        self.assertEqual(actual, expected)

    def test_concatenate_lists_multi_elements(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()
        l.add_first(10)
        l.add_first(20)
        l.add_first(30)
        m.add_first(40)
        m.add_first(50)
        m.add_first(60)
        actual = concatenate_lists(l.head, m.head)
        expected = [30, 20, 10, 60, 50, 40]
        self.assertEqual(actual, expected)