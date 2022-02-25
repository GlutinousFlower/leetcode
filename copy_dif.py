# -*- coding: utf-8 -*-
# @Time : 2022/1/12 2:56 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : copy_dif.py


# 深拷贝浅拷贝
import copy

a = [1, 2, 3, ['a', 'b']]
b = copy.copy(a)
c = copy.deepcopy(a)
a.append(4)
b[3].append('c')
print(a)
print(b, c)

# 修改python函数里的全局变量
i = 0


def area(x, y):
    # global i
    i = x * y
    return i


a = b = 3
print(area(a, b))

# re模块的match和search
import re

a = re.match('hello', 'hhdshello')
b = re.search('hello', 'hhdshello').span()
print(a, b)

# lambda使用
from functools import reduce

# l = [1, 2, 3, 4, 5, 6, 7, 8]
li = [1, 2, 3, 4, 5]
# 序列中的每个元素加1
map(lambda x: x + 1, li)  # [2,3,4,5,6]
# 返回序列中的偶数
filter(lambda x: x % 2 == 0, li)  # [2, 4]
# 返回所有元素相乘的结果
reduce(lambda x, y: x * y, li)  # 1*2*3*4*5 = 120

a = lambda x: -li[1]
print(a(0))
