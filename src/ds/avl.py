from __future__ import annotations

from typing import Any

from .binary_tree import TreeNode


class AVLNode(TreeNode):
    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.p: AVLNode = None
        self.balance = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(val={self.value}, balance={self.balance})"


class AVLTree:
    def __init__(self) -> None:
        self.root: AVLNode | None = None

    @classmethod
    def fromarray(cls, arr: list[Any]) -> AVLTree:
        tree = cls()

        for value in arr:
            tree.insert(value)

        return tree

    def lr(self, node: AVLNode) -> None:
        y = node.right

        node.right = y.left

        if y.left is not None:
            y.left.p = node

        y.p = node.p

        if node.p is None:
            self.root = y

        elif node is node.p.left:
            node.p.left = y
        else:
            node.p.right = y

        y.left = node
        node.p = y

    def rr(self, node: AVLNode) -> None:
        x = node.left

        node.left = x.right

        if x.right is not None:
            x.right.p = node

        x.p = node.p

        if node.p is None:
            self.root = x
        elif node is node.p.right:
            node.p.right = x
        else:
            node.p.left = x

        x.right = node
        node.p = x

    def _update_balance(self, ya: AVLNode, z: AVLNode) -> None:
        y = ya.left if z.value < ya.value else ya.right

        while y is not z:
            if z.value < y.value:
                y.balance = 1
                y = y.left
                continue

            y.balance = -1
            y = y.right

    def _imbalance_dir(self, ya: AVLNode, z: AVLNode) -> int:
        if z.value < ya.value:
            return 1

        return -1

    def _handle_left_subtree(self, ya: AVLNode, s: AVLNode, i: int) -> None:
        if i == 1:
            self.rr(ya)
        else:
            self.lr(ya)

        ya.balance = 0
        s.balance = 0

    def _handle_right_subtree(self, ya: AVLNode, s: AVLNode, i: int) -> None:
        if i == 1:
            p = s.right
            self.lr(s)
            self.rr(ya)
        else:
            p = s.right
            self.rr(s)
            self.lr(ya)

        if p.balance == 0:
            ya.balance = 0
            s.balance = 0
        elif p.balance == i:
            ya.balance = -i
            s.balance = 0
        else:
            ya.balance = 0
            s.balance = i

        p.balance = 0

    def _avl_fixup(self, ya: AVLNode, z: AVLNode) -> None:
        s = ya.left if z.value < ya.value else ya.right

        i = self._imbalance_dir(ya, z)

        if s.balance == i:
            return self._handle_left_subtree(ya, s, i)

        return self._handle_right_subtree(ya, s, i)

    def insert(self, value: Any) -> AVLNode:
        z = AVLNode(value=value)

        if self.root is None:
            self.root = z
            return

        y = None
        x = self.root

        ya = x

        while x is not None:
            y = x
            x = x.left if value < x.value else x.right

            if x is not None and x.balance != 0:
                ya = x

        z.p = y

        if z.value < y.value:
            y.left = z
        else:
            y.right = z

        self._update_balance(ya, z)

        i = self._imbalance_dir(ya, z)

        if ya.balance == 0:
            ya.balance = i
            return

        if ya.balance != i:
            ya.balance = 0
            return

        return self._avl_fixup(ya, z)
