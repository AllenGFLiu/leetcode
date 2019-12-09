'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

from typing import Optional

# 思路：
# 用变形的双指针：从头到尾遍历子串，截取当前index到子串末尾的字段
# 再用一头一尾两个指针表示字段的头和尾字符，如果不相等，尾变量--；如果相等，截取并reverse后对比是否相等
# 另外，根据题目要求寻找最长的子串，所以引入max_count变量
# 时间复杂度 O(n^3)，空间复杂度O(n)

# 还有一个Manacher算法，可以了解下
def longestPalindrome(self, s: str) -> str:
    count = len(s)
    if not count or count == 1:
        return s
    p= 0
    max_count = 0
    max_str = ''
    while p < len(s)-1:
        new_s = s[p:]
        i = 0
        j = len(new_s)-1
        while j > i:
            if new_s[j] == new_s[i]:
                reverse_s = new_s[i:j+1][::-1]
                if reverse_s == new_s[i:j+1] and j-i+1>max_count:
                    max_count = j-i+1
                    max_str = reverse_s
            j -= 1
        p += 1
    return max_str if max_count > 1 else s[0]
