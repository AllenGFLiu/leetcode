class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def swap(head):
    if not head or not head.next:
        return head

    p = ListNode(None)
    curr, head, stack = head, p, []
    while curr and curr.next:
        curr_next = curr.next
        curr.next = None
        stack.append(curr)
        curr_next_next = curr_next.next
        curr_next.next = None
        stack.append(curr_next)
        p.next = stack.pop()
        p.next.next = stack.pop()

        p = p.next.next
        curr = curr_next_next

    p.next = curr if curr else None
    return head.next


if __name__ == '__main__':
    head = ListNode(1)
    next = ListNode(2)
    head.next = next
    swap(head)