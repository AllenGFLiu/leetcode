'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''

# 思路:这种数的比对大家都知道肯定需要用递归
# 但这道题在从上往下递归的时候需要保留上一层的值用来跟本层比对： 本层是左子节点的时候，本节点的值要小于父节点的值
# 本层是右子节点的时候，本节点的值要大于父节点的值，但问题又来了
# 怎么判断左右子树种的所有节点都满足跟祖父节点的大小关系？
# 单纯传递一个界限值，显然无法满足了，需要传两个：一个上限，一个下限
# 比如root节点的右子树的左节点的下限就是root节点值，上限就是其父节点的节点值
def isValidBST(self, root: TreeNode) -> bool:
    def helper(node, lower_limit=float('inf'), upper_limit=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower_limit or val >= upper_limit:
            return False

        if not helper(node.left, lower_limit, node.val):
            return False

        if not helper(node.right, node.val, upper_limit):
            return False

        return True

    return helper(root)
