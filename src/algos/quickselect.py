import random
from typing import TypeVar

from src.algos import partition
from src.types import Comparable

T = TypeVar("T", bound=Comparable)


def randomized_quickselect(A: list[T], l: int, r: int, k: int) -> T:
    if k > 0 and k <= (r - l + 1):
        pivot_idx = random.randint(l, r)

        A[r], A[pivot_idx] = A[pivot_idx], A[r]

        q = partition(A, l, r)

        pivot_rank = 1 + (r - q)

        if k == pivot_rank:
            return A[q]

        if k < pivot_rank:
            return randomized_quickselect(A, q + 1, r, k)

        return randomized_quickselect(A, l, q - 1, k - pivot_rank)
