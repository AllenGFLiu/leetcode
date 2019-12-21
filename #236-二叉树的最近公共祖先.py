'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉中。
'''

from typing import Optional


# 235题中给定的是二叉搜索树，本题给定的是二叉树
# 针对树的操作，一般都是以递归切入最好解决
# 本题意思就是给定一个根节点，在根节点的左右子树中分别查找p和q节点
# 如果查找左右子树都能返回实际的节点，说明此节点就是公共节点
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.lfet, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left if left else right