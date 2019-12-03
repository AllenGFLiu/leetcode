'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''

from typing import Optional


# 先排序，后比较相邻元素是否相等
# 时间复杂度利用加法规则，主要依赖排序时间复杂度
# 空间复杂度O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for index in range(len(nums)-1):
        if nums[index+1] == nums[index]:
            return True
    return False


# 使用哈希表
# 时间复杂度O(n)
# 空间复杂度O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    d = {}
    for num in nums:
        if num in d:
            return True
        d[num] = 'True'
    return False


# 利用set容器内的元素不能重复的特性
# 时间复杂度O(n)
# 空间复杂度O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    s = set(nums)
    return len(nums) != len(s)