'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

# 与#2两数相加同样的思路
# 双指针
def addStrings(self, num1: str, num2: str) -> str:
    i = len(num1)-1
    j = len(num2)-1
    carry = 0
    res = ''
    while i >= 0 or j >= 0:
        v_i = int(num1[i]) if i >= 0 else 0
        v_j = int(num2[j]) if j >= 0 else 0
        sum_value = v_i + v_j + carry
        carry = sum_value // 10
        res = str(sum_value%10) + res
        i -= 1
        j -= 1
    
    if carry>0:
        res = '1' + res

    return res