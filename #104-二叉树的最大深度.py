'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

# 借助广度优先搜索算法遍历二叉树的层，最后返回层数
def max_depth(root):
    if not root: return 0

    queue = [root]
    res = 0
    while queue:
        stack = []
        res += 1
        for node in stack:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        queue = stack
    return res


# 递归，树的层数就是根节点的层数，根节点的层数就是左右子树中层数最大的再加 1。
def max_depth(root):
    def count(node):
        if not node: return 0
        left_count = count(node.left)
        right_count = count(node.right)
        return 1 + max(left_count, right_count)

    return count(root)