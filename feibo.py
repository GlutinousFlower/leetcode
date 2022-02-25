# -*- coding: utf-8 -*-
# @Time : 2022/2/11 3:10 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : feibo.py

"""
青蛙跳台阶问题
"""


def get_jump_time(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return get_jump_time(n - 1) + get_jump_time(n - 2)


print(get_jump_time(100))