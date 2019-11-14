'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''

from typing import Optional


def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if m == n: return head

    new_node = ListNode(None)
    new_node.next = head
    prev = new_node

    for i in range(m-1):
        prev = prev.next

    reverse_node = None
    cur = prev.next
    for i in range(n-m+1):
        next = cur.next
        cur.next = reverse_node
        reverse_node = cur
        cur = next

    prev.next.next = cur
    prev.next = reverse_node

    return new_node.next