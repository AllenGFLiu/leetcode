'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l, r):
            tmp_head = ListNode(None)
            tmp_tail = tmp_head
            while l and r:
                if l.val < r.val:
                    tmp_tail.next = l
                    l = l.next
                else:
                    tmp_tail.next = r
                    r = r.next
                tmp_tail = tmp_tail.next
            return tmp_head.next


        def cut(node, step):
            i = 1
            while i < step and node:
                i += 1
                node = node.next
            if not node:
                return node
            tmp, node.next = node.next, None
            return tmp

        if not head or not head.next:
            return head

        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next

        dummy_head = ListNode(None)
        dummy_head.next = head
        bs = 1
        while bs < count:
            curr = dummy_head.next
            tail = dummy_head
            while curr:
                left = curr
                right = cut(left, bs)
                curr = cut(right, bs)
                tail.next = merge(left, right)
                while tail.next:
                    tail = tail.next
            bs <<= 1

        return dummy_head.next