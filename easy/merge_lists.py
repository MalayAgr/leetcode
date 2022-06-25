class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(val={self.val})"


def merge_sorted_lists(list_a: ListNode | None, list_b: ListNode | None):
    curr_a = list_a
    curr_b = list_b

    if curr_a is None and curr_b is not None:
        return curr_b

    if curr_a is not None and curr_b is None:
        return curr_a

    if curr_a is None and curr_b is None:
        return None

    result = ListNode(-1)
    curr_res = result

    while curr_a is not None and curr_b is not None:
        if curr_a.val <= curr_b.val:
            curr_res.next = curr_a
            curr_res, curr_a = curr_res.next, curr_a.next
        else:
            curr_res.next = curr_b
            curr_res, curr_b = curr_res.next, curr_b.next

    longer = curr_b if curr_a is None else curr_a
    curr_res.next = longer

    result = result.next

    return result


if __name__ == "__main__":
    l1 = ListNode(val=1)
    temp = l1

    for i in (2, 3, 5):
        temp.next = ListNode(val=i)
        temp = temp.next

    l2 = ListNode(val=0)
    temp = l2

    for i in (2, 4):
        temp.next = ListNode(val=i)
        temp = temp.next

    result = merge_sorted_lists(list_a=l1, list_b=l2)
    temp = result

    while temp is not None:
        print(temp.val)
        temp = temp.next
