from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from src.exceptions import UnderflowError


class ListNode:
    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.next: ListNode = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"


class LinkedList:
    def __init__(self) -> None:
        self.head: ListNode = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(head={self.head})"

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value: Any = None) -> ListNode:
        node = ListNode(value=value)
        node.next = self.head
        self.head = node
        return node

    def insert_after(self, node: ListNode, value: Any = None) -> ListNode:
        new_node = ListNode(value=value)
        new_node.next = node.next
        node.next = new_node
        return new_node

    def pop(self) -> ListNode:
        if self.is_empty():
            raise UnderflowError("The list is empty.")

        node = self.head
        self.head = self.head.next

        return node

    def delete_after(self, node: ListNode) -> ListNode:
        if node.next is None:
            msg = "There is no node after the given node."
            raise UnderflowError(msg)

        deleted_node = node.next
        node.next = deleted_node.next

        return deleted_node

    def __iter__(self) -> Iterator[ListNode]:
        curr = self.head

        while curr is not None:
            yield curr
            curr = curr.next
