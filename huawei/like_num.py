# -*- coding: utf-8 -*-
# @Time : 2022/1/13 4:39 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : like_num.py

# s=input()
# a=float(s)
# print(a)

def num_reserve(num):
    l=list(str(num))
    l1=[]
    if len(l)==1:
        return num
    else:
        l1=l[::-1]
        print(''.join(l1))



if __name__ == '__main__':
    num_reserve(756794)


