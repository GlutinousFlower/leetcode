# -*- coding: utf-8 -*-
# @Time : 2022/1/6 4:18 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : sum_ascii.py


"""
输入描述：
输入一行没有空格的字符串。

输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。

示例1
输入：abc
输出：3
示例2
输入：aaa
输出：1
"""
s=input()
j=0
for i in set(s):
    if 0<=ord(i)<=127:
        j+=1
print(j)

