'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''

from typing import Optional

# 题意要求不要使用除法，意思就是先对全部元素做乘积，然后再遍历每个元素，相除即可
# 另外一种解法
# 先从左到右遍历，保存当前元素左侧元素的乘积
# 然后从右到左遍历，保存当前元素右侧元素的乘积
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    k = 1
    res = [0] * n

    for i in range(n):
        res[i] = k
        k *= nums[i]

    k = 1
    for j in range(n-1, -1, -1):
        res[j] *= k
        k *= nums[i]

    return res
