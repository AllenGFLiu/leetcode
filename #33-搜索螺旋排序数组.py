'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''


def search(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        midd = low + ((high-low)>>1)
        if nums[midd] == target:
            return midd
        if nums[midd] > nums[high]:
            # 前半有序后半旋转

            # 在前半中用二分查找，否则去后半
            if target >= nums[low] and target < nums[midd]:
                high = midd - 1
            else:
                low = midd + 1
        elif nums[midd] < nums[low]:
            # 后半有序前半旋转

            # 在后半中用二分查找，否则去前半
            if target <= nums[high] and target > nums[midd]:
                low = midd + 1
            else:
                high = midd - 1
        else:
            # 经过前边的边界判定后进入如下的二分查找判断
            if target > nums[midd]:
                low = midd + 1
            else:
                high = midd - 1
    return -1