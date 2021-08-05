import unittest


class EmptyLinkedListException:
    pass


class DummyNode:
    def __init__(self, element, _next):
        self.element = element
        self.next = _next


class SinglyLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

        @property
        def next(self):
            return self._next

        @property
        def element(self):
            return self._element

    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        new_head = self._Node(element, self.head)
        old_head = self.head
        self.head = new_head
        self.head._next = old_head
        self._size += 1

    def add_last(self, element):
        new_node = self._Node(element, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail._next = new_node
        self.tail = new_node
        self._size += 1

    def remove_first(self):
        """ It doesn't mean to remove the node from the memory, only remove the next pointer,
         and trust your garbage collector """
        if self.is_empty():
            raise EmptyLinkedListException
        new_head = self.head._next
        self.head._next = None
        self.head = new_head
        self._size -= 1


class TestSinglyLinkedList(unittest.TestCase):
    # ===== testing Add_Last =====
    def test_add_last(self):
        pass

    # ===== testing Add_First =====
    def test_add_first_no_head(self):
        s = SinglyLinkedList()
        actual = s.head
        expected = None
        self.assertEqual(actual, expected)

    def test_add_first_one_head(self):
        s = SinglyLinkedList()
        s.add_first(1)
        actual = s.head._element
        expected = 1
        self.assertEqual(actual, expected)

    def test_add_first_two_head(self):
        s = SinglyLinkedList()
        s.add_first(2)
        s.add_first(1)
        actual = s.head._element
        expected = 1
        self.assertEqual(actual, expected)

    def test_add_first_multi_head(self):
        s = SinglyLinkedList()
        for i in range(10):
            s.add_first(i)
        actual = s.head._element
        expected = 9
        self.assertEqual(actual, expected)

class TestDummyNode(unittest.TestCase):
    pass