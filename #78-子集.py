'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


# Solution1:内置函数
def subsets(nums):
    n = len(nums)
    res = []
    for i in range(n+1):
        for num in itertools.combinations(nums, i):
            res.append(num)

    return res


# Solution2-1:递归
# Tips:列表作为全局变量使用
def subsets(nums):
    n = len(nums)
    res = []
    stack = []

    def helper(i):
        res.append(stack[:])

        for j in range(i, n):
            if nums[j] not in stack:
                stack.append(nums[j])
            helper(j+1)
            stack.pop()

    helper(0)
    return res


# Solution2-2:递归
# 列表作为函数参数使用
def subsets(nums):
    n = len(nums)
    res = []

    def helper(i, stack):
        res.append(stack)

        for j in range(i, n):
            helper(j+1, stack+[nums[j]])

    helper(0, [])
    return res