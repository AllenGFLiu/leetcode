'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

# Pythonic版
def longestCommonPrefix(strs):
    if not strs: return ''

    shortest = min(strs, key=len)
    for index, char in enumerate(shortest):
        for one_str in strs:
            if one_str[index] != char:
                return shortest[:index]
    return shortest


def longestCommonPrefix(strs):
    count = len(strs)
    if count == 0: return ''
    if count == 1: return strs[0]
    result = ''
    for index in range(len(strs[0])):  # 以strs的第一个字符串元素为基准
        tmp_count = 1
        for num in range(1, count):  # 循环比对strs剩余的字符串元素
            equal = False
            if len(strs[num]) >= index+1:  # 防止第二个或者之后的字符串元素的长度比第一个短，造成list越界
                if strs[num][index] == strs[0][index]:
                    tmp_count += 1  
                    equal = True
                    continue
        
        if index == 0 and not equal:  # 如果与第一个字符串元素的第一个字符就不相等，那就可以直接退出了
            return result

        if equal and tmp_count == count:  # 防止strs中间有空元素，比如['abc', '', 'ab']
            result += strs[0][index]

    return result
