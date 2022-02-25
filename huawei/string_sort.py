# -*- coding: utf-8 -*-
# @Time : 2022/1/6 4:25 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : string_sort.py

"""
字串的连接最长路径查找？给定n个字符串，
请对n个字符串按照字典序排列。输入描述:输入第一行为一个正整数n(1≤n≤1000),
下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。输出描述:数据输出n行，输出结果为按照字典序排列的字符串。
"""
# n=input()
# lis=[]
# for i in range(int(n)):
#     lis.append(input())
# lis.sort()
# for i in range(int(n)):
#     print(lis[i],end='\n')

num = int(input())
in_list = [input() for x in range(num)]
in_list_s = ['app','ab','hsk','year','test','yaml']
in_list_s = sorted(in_list)
for x in in_list_s:
    print(x)
