import sys
from collections import deque

sys.path.insert(0, "/media/malay_agr/Shared/Coding/Python/leetcode")

from src.ds import AVLTree


def sorted_array_to_bst(nums: list[int]):
    tree = AVLTree.fromarray(nums)
    return tree.root


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]

    result = sorted_array_to_bst(nums=nums)

    queue = deque()
    queue.append(result)

    while queue:
        node = queue.pop()
        print(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
