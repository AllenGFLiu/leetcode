'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

from typing import Optional

def reverse(x: int) -> int:
    fu = False
    if x < 0:
        fu = True
        x = -x

    new_int = 0
    while x // 10:
        new_index = x % 10
        new_int = (new_int + new_index) * 10

        x = x // 10
    
    new_int += x

    if new_int >= pow(2, 31):
        return 0

    return -new_int if fu else new_int