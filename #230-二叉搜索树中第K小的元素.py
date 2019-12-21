'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
'''

from typing import Optional

# 中序遍历二叉树，设定全局count变量，当count == k 时保存当时节点变量的值，并退出递归
def kthSmallest(self, root: TreeNode, k: int) -> int:
    def inorder(node):
        nonlocal count
        if not node or count == k:
            return
        
        inorder(node.left)
        count += 1
        if count == k:
            res.append(node.val)
            return
        inorder(node.right)

    count = 0
    res = []
    inorder(root)
    return res[0]