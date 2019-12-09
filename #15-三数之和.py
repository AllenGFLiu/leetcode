'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

from typing import Optional

def threeSum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    if n < 3:
        return []

    res = []
    nums.sort()  # 先把原序列转成有序列

    for k in range(n-2):
        if nums[k] > 0: break  # 因为是有序列，三数中最小的一个都已经大于0了，其和肯定不会等于0了，所以可以直接break了
        if k > 0 and nums[k] == nums[k-1]: continue  # 因为题目要求不要有重复的，所以continue即可

        start, end = k+1, n-1 # 固定K，然后动态移动start和end双指针
        while start < end:
            sum_value = nums[k] + nums[start] + nums[end]
            if sum_value > 0:
                end -= 1
                while start < end and nums[end+1] = nums[end]:  # 排序之和，相等的元素会在一起，按照题目要求不要有重复的，所以就可以跳过了
                    end -= 1
            elif sum_value < 0:
                start += 1
                while start < end and nums[start-1] = nums[start]:
                    start += 1
            else:
                res.append([nums[k], nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start-1] == nums[start]:
                    start += 1
                while start <end and nums[end+1] = nums[end]:
                    end -= 1
    return res