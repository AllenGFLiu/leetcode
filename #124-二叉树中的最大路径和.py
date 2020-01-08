'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
'''

def math_path_sum(root):
    def helper(node):
        if not node: return 0
        left = helper(node.left)
        right = helper(node.right)

        self.res = max(left+node.val+right, self.res)
        return max(0, max(left, right)+root.val)

    self.res = float('-inf')
    helper(root)
    return self.res