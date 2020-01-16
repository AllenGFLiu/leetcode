'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''


# 鸽巢原理
# 正确的顺序应该是对应编号的格子呆在对应编号的巢里
# 对应到数组中，就是应该是nums[i] = i+1(编程语言中的数组一般都是从0开始的)
# 第一个循环是把打乱的鸽子放回到原本该呆在的巢里
# 第二个循环是查看对应标号的巢中呆的鸽子是不是本编号的鸽子，如果不是，就是缺失的鸽子
def findDisappearedNumbers(nums):
    res=[]
    for i in range(len(nums)):
        while(nums[i] != i+1 and nums[i] != nums[nums[i]-1]):
            nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
    
    for i in range(len(nums)):
        if(nums[i] != i+1):
            res.append(i+1)
    return res


if __name__ == '__main__':
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))