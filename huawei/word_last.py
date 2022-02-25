# -*- coding: utf-8 -*-
# @Time : 2022/1/6 3:50 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : word_last.py

num = input()
num = num[::-1]

num1 = list(set(num))

num1.sort(key=num.index)
# print(num1)
print(''.join(num1))
