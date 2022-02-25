# -*- coding: utf-8 -*-
# @Time : 2022/2/14 5:45 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : longest_huiwen.py

"""
最长回文子串
"""


def longestPalindrome( s: str) -> str:
    size = len(s)  # 首先得到字符串的长度，方便逐个点遍历
    res = []  # 因为要返回一个最长子串，所以初始化一个返回参数
    max_val = 0

    def num(loc_left, loc_right):  # 定义一个以某个点为中心，寻找最长子串的函数
        while loc_left >= 0 and loc_right < size:  # 因为要找到最长子串，所以要利用while函数不停的往两个方向寻找
            if s[loc_left] == s[loc_right]:  # 如果左边点与右边点的元素相同，则继续往两边遍历
                loc_left -= 1  # 往两边遍历，自然就是左边角标减1
                loc_right += 1  # 往两边遍历，自然就是右边角标加1
            else:  # 如果发现不一样的，直接跳出，说明不是回文串
                break
        return s[loc_left + 1: loc_right]  # 函数的返回值即为我们找到的以当前点为中心的最常子串

    for i in range(size):  # 因为要以每个点为中心寻找，自然要逐个遍历
        res1 = num(i, i)  # 此时为奇数情况，以一个点为中心
        res2 = num(i, i + 1)  # 此时为偶数情况，以相邻两个点为中心
        if max(len(res1), len(res2)) > max_val:  # 比较两种情况为中心返回的最长子串的长度
            max_val = max(len(res1), len(res2))  # 如果当前返回长度比之前的大，则更新max_val，即最长子串的长度
            if len(res1) > len(res2):  # 此时判断是哪种情况的子串长，更新返回函数
                res = res1
            else:
                res = res2
    return res  # 返回的即为最长子串


if __name__ == '__main__':
    print(longestPalindrome('qwereeresdsdsas'))

