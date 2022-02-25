# -*- coding: utf-8 -*-
# @Time : 2022/1/6 5:06 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : test.py

def get_last_num(n):
    l=[1,4,5,9,6,3,-1]
    c=[]
    for i in l:
        j=i-n
        c.append(abs(j))

    print(l[c.index(min(c))])

if __name__ == '__main__':
    get_last_num(6)


