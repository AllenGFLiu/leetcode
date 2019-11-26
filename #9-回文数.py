'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''


# 如下使用数学方法实现
# 也可以使用空间复杂度比较高的转字符串处理的方法
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False

    curr = 0
    tmp = x
    while tmp // 10:
        curr = (curr+ tmp%10) * 10
        tmp = tmp // 10
    curr += tmp%10

    return curr == x