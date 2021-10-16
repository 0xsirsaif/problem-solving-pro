""""

"""


class MyLinkedList:
    class _Node:
        __slots__ = "val", "next_"

        def __init__(self, value, next_):
            self.val = value
            self.next_ = next_

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ptr = self.head
        idx = 1
        while ptr:
            if idx == index:
                return ptr.val
            ptr = ptr.next_
            idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_head = self._Node(val, self.head)
        self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = self._Node(val, None)
        if not self.tail:
            self.head.next_ = new_tail
        else:
            self.tail.next_ = new_tail

        self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        ptr = self.head
        idx = 1
        prev_node = None
        while ptr:
            if idx == index - 2:
                prev_node = ptr
            ptr = ptr.next_
            idx += 1

        if prev_node:
            next_node = prev_node.next_
            prev_node.next_ = self._Node(val, next_node)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.size < index:
            return
        ptr = self.head
        idx = index - 1
        prev_node = None
        while ptr:
            if idx == index:
                prev_node = ptr
            ptr = ptr.next_
            idx += 1

        if prev_node:
            deleted_node = prev_node.next_
            next_node = deleted_node.next_
            prev_node.next_ = next_node
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
