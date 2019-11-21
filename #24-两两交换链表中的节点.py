'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

from typing import Optional


# 递归实现
def swapPairs(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    next = head.next
    head.next = swapPairs(next.next)
    next.next = head

    return next


#  利用栈,迭代反转
def swapPairs(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head

    p = ListNode(None)
    cur, head, stack = head, p, []
    while cur and cur.next:
        cur_next = cur.next
        cur.next = None
        stack.append(cur)
        cur_next_next = cur_next.next
        cur_next.next = None
        stack.append(cur_next)
        cur = cur_next_next
        p.next = stack.pop()
        p.next.next = stack.pop()
        p = p.next.next


# 迭代解决
# 思路:pre->a->b->b.next 变更为 pre—>b->a->b.next
def swapPairs(self, head: ListNode) -> ListNode:
    pre = self
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next

        pre = a
    return self.next

    p.next = cur if cur else None
    return head.next
