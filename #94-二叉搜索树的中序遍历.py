'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

# 递归实现
def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    res = []
    inorder(root)
    return res

# 迭代实现
def inorderTraversal(self, root: TreeNode) -> List[int]:
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if color == WHITE:
            if node:
                if node.right:
                    stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                if node.left:
                    stack.append((WHITE, node.left))
        elif color == GRAY:
            res.append(node.val)
    return res