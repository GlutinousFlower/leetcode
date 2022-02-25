# -*- coding: utf-8 -*-
# @Time : 2022/1/10 11:55 上午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : zumu_sort.py

while True:
    try:
        s = input()
        zimu = ''
        f = ''
        for i in s:
            if i.isalpha():
                zimu += i
        zmpx = sorted(zimu, key=str.upper)
        f = ''
        idx = 0
        for i in range(len(s)):
            if s[i].isalpha():
                f += zmpx[idx]
                idx += 1
            else:
                f += s[i]
        print(f)
    except:
        break
