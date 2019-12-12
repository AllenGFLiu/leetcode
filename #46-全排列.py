'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

from typing import Optional

def permute(nums):
    def backtrack():
        if len(track) == len(nums):
            res.append(track[:])
            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue

            track.append(nums[i])
            backtrack()
            track.pop()

    res = []
    track = []
    backtrack()
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(nums))