from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from .stack import Stack


class TreeNode:
    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"


class BinaryTree:
    def __init__(self) -> None:
        self.root: TreeNode = None

    def is_empty(self) -> bool:
        return self.root is None

    def _is_equal(self, a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True

        if a is not None and b is not None:
            return (
                a.value == b.value
                and self._is_equal(a.left, b.left)
                and self._is_equal(a.right, b.right)
            )

        return False

    def __eq__(self, other: BinaryTree) -> bool:
        return self._is_equal(self.root, other.root)

    @classmethod
    def fromarray(cls, values: list[Any]) -> BinaryTree:
        nodes = [(TreeNode(value=val), None)[val is None] for val in values]
        n = len(nodes)

        for idx, node in enumerate(nodes):
            if node is None:
                continue

            l_idx = 2 * idx + 1

            if l_idx < n:
                node.left = nodes[l_idx]

            r_idx = l_idx + 1

            if r_idx < n:
                node.right = nodes[r_idx]

        tree = cls()
        tree.root = nodes[0]

        return tree

    def preorder(self) -> Iterator[TreeNode]:
        if self.root is None:
            yield from ()
            return

        stack: Stack[TreeNode] = Stack()
        stack.push(self.root)

        while stack:
            node = stack.pop()
            yield node

            if node.right is not None:
                stack.push(node.right)

            if node.left is not None:
                stack.push(node.left)

    def inorder(self) -> Iterator[TreeNode]:
        if self.is_empty():
            yield from ()
            return

        node = self.root

        stack: Stack[TreeNode] = Stack()

        while node is not None or stack:
            if node is not None:
                stack.push(node)
                node = node.left
                continue

            node = stack.pop()
            yield node

            node = node.right

    def postorder(self) -> Iterator[TreeNode]:
        if self.root is None:
            yield from ()
            return

        node = self.root
        stack: Stack[TreeNode] = Stack()

        while True:
            while node is not None:
                if node.right is not None:
                    stack.push(node.right)

                stack.push(node)

                node = node.left

            node = stack.pop()

            tos = stack.tos(ignore_uf=True)

            if node.right is not None and tos is node.right:
                stack.pop()
                stack.push(node)
                node = node.right
                continue

            yield node

            node = None

            if not stack:
                break

    def _is_balanced_helper(self, node: TreeNode) -> int:
        if node is None:
            return 0

        l_height = self._is_balanced_helper(node.left)

        if l_height == -1:
            return -1

        r_height = self._is_balanced_helper(node.right)

        if r_height == -1:
            return -1

        if abs(l_height - r_height) > 1:
            return -1

        return 1 + max(l_height, r_height)

    def is_balanced(self) -> bool:
        result = self._is_balanced_helper(self.root)
        return result == -1
