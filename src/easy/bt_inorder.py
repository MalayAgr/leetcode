from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode = None, right: TreeNode = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    node = root

    result = []

    stack = []

    while node is not None or stack:
        if node is not None:
            stack.append(node)
            node = node.left
            continue

        node = stack.pop()
        result.append(node.val)

        node = node.right

    return result


def make_tree(values: list[int]) -> TreeNode:
    n = len(values)
    nodes = [(TreeNode(val=val), None)[val is None] for val in values]

    for idx, node in enumerate(nodes):
        if node is None:
            continue

        l_idx = 2 * idx + 1

        if l_idx < n:
            node.left = nodes[l_idx]

        r_idx = l_idx + 1

        if r_idx < n:
            node.right = nodes[r_idx]

    return nodes[0]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, None, 7, None, None, 6]
    root = make_tree(values=values)
    print(inorder(root=root))
