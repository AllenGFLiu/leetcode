'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

进阶：
你是否可以不用额外空间解决此题？
'''

# 仔细审题，题目要求是返回入环的第一个节点
# 141题是检测是否有环
# 本题是在检测到有环后，找到入环的第一个元素
# 所以算法分两阶段执行
def detectCycle(self, head: ListNode) -> ListNode:
    # 阶段一：检测是否有环存在
    slow, fast = head, head
    while True:
        if not fast or not fast.next: return  # 无环
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break  # 检测到有环的存在
    # 阶段二： 找到入环的第一个元素
    third = head  # 从slow和fast相遇的节点开始，另外声明third节点从head， 
    # 二者各走一步，待相遇时就是所求的节点
    while third != slow:
        slow = slow.next
        third = third.next
    return slow  # 此时slow和third时一样，都是入环的第一个节点