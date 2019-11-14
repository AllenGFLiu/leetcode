'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

from typing import Optional


def reverseList(self, head: ListNode) -> ListNode:
    reverse_node = None
    while head:
        next = head.next
        head.next = reverse_node
        reverse_node = head
        head = next
    return reverse_node