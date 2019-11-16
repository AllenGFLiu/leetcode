'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

from typing import Optional


# 把原来的链表打造成一个环(指定最后一个节点指向第一个节点)
# 通过规律，定位新的头结点和尾节点,最后返回新的头结点即可
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head: return
    if not head.next: return head

    tmp_node = head
    count = 1
    while tmp_node.next:
        tmp_node = tmp_node.next
        count += 1
    tmp_node.next = head

    k = k%count
    new_tail = head
    for _ in range(count-k-1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    return new_head


# 仿照旋转数组(#189)解法
# 先整体反转原始链表,再旋转(1, k),最后再旋转(k+1, count)即可。
def rotateRight(self, head: ListNode, k: int) -> ListNode:

    def reverse_between(head, m, n):
        if m == n: return head

        new_node = ListNode(None)
        new_node.next = head
        prev = new_node

        for _ in range(m-1):
            prev = prev.next

        curr = prev.next
        reverse_node = None
        for _ in range(n-m+1):
            next = curr.next
            curr.next = reverse_node
            reverse_node = curr
            curr = next

        prev.next.next = curr
        prev.next = reverse_node

        return new_node.next

    if not head: return
    if not head.next: return head

    tmp = head
    count = 1
    while tmp.next:
        tmp = tmp.next
        count += 1

    k = k%count
    if not k: return head
    new_node = reverse_between(head, 1, count)
    new_node = reverse_between(new_node, 1, k)
    new_node = reverse_between(new_node,k+1, count)
    return new_node