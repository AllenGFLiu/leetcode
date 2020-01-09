'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
'''

# 樹上的遍歷一般都是遞歸
# 遞歸邏輯:
# 遞推公式:遞歸判斷左子樹中路徑和是否等於總和減去某節點的val值,右子樹同理,並且左右子樹中只要有一個為True,則結果為True
# 終止條件:在遞歸到葉子節點時才執行判斷遞減下來的值是否等於本節點的val值,否則就是一直遞減下去.
def hasPathSum(root, sum):
    def helper(node, target):
        if not node:
            return False

        if not node.left and not node.right:
            return node.val == target

        return helper(node.left, target-node.val) or helper(node.right, target-node.val)

    return helper(root, sum)


# 上面的方法是遞減下去
# 本方法原理一直,只不過是遞增下去
def hasPathSum(root, sum):
    def helper(node, tmp):
        if not node:
            return False

        if not node.left and not node.right:
            return tmp+node.val == sum

        return helper(node.left, tmp+node.val) or helper(node.right, tmp+node.val)

    return helper(root, 0)