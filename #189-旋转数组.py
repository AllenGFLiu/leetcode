'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
'''
# -*- coding:utf-8 -*-


from typing import Optional


# 方法1
# 时间复杂度 O(n)
# 空间复杂度 O(n)
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    new_nums = nums.copy()
    count = len(nums)
    if count == 0:
        return
    new_nums.extend(new_nums)
    i = count - k % count
    j = 0
    while j < count:
        nums[j] = new_nums[i+j]
        j += 1


# 方法2
# 时间复杂度 O(n)
# 空间复杂度 O(1)
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    count = len(nums)
    if count == 0:
        return

    k %= count

    reverse(nums, 0, count-1)
    reverse(0, k-1)
    reverse(k, count-1)
