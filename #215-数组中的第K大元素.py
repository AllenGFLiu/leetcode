'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''

from typing import Optional

# Solution 1: use built_in function to sort origin array, then locate -Kth num
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]

# Solution 2: use quickSort algorithm to divide origin array into three parts:[0...q-1] [q] [q+1...len(nums)-1]
# the [0...q-1] part is smaller than [q] , the [q+1...len(nums)-1] part is bigger than [q]
# the question is looking for kth biggest item, that means it is (len(nums)-k) smallest item(count from 0)
def findKthLargest(self, nums: List[int], k: int) -> int:
    def partition(nums, p, r):
        pivot = nums[r]
        i = p
        for j in range(p, r+1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def divide(nums, p, r):
        if p >= r: return nums[p]

        q = partition(nums, p, r)
        if q == kth_smallest:
            return nums[q]
        elif q < kth_smallest:
            return divide(nums, q+1, r)
        elif q > kth_smallest:
            return divide(nums, p, q-1)


    kth_smallest = len(nums)-k
    return divide(nums, 0, len(nums)-1)
