'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''


# 這是一道 hard 題目,方法卻有很多,有最簡單暴力的,還有用優先級隊列的
# 總結一下經驗就是:後續遇到題目,要從多個角度和方向去想,然後對比孰優孰劣

# solution1:簡單暴力. 遍歷,然後插入元素到一個整合的list中,根據該list再構建一個新排序鏈錶返回
def mergeKLists(lists):
    res = []
    for one_list_node in lists:
        node = one_list_node
        while node:
            res.append(node.val)
            node = node.next

    dummy = ListNode(None)
    pre = dummy
    for value in res:
        pre.next = ListNode(value)
        pre = pre.next

    return dummy.next


# solution2:優先級隊列
# 借用了優先級隊列時間複雜度為 O(logn) 的排序複雜度,可以直接拿到最小元素
def mergeKList(lists):
    import queue
    q = queue.PriorityQueue()

    for index, one_list_node in enumerate(lists):
        if one_list_node:
            q.put((one_list_node.val, index, one_list_node))

    dummy = ListNode(None)
    pre = dummy
    while not q.empty():
        node = q.get()
        pre.next = ListNode(node[0])
        pre = pre.next
        if node[2].next:
            q.put(node[2].next.val, node[1], node[2].next)

    return dummy.next