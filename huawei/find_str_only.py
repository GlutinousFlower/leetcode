# -*- coding: utf-8 -*-
# @Time : 2022/1/10 3:53 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : find_str_only.py

while True:
    try:
        s = input()
        l = {}
        for i in range(len(s)):
            number = s.count(s[i])
            l.setdefault(s[i], number)
        # print(l)

        flag = False
        for item in l.items():
            if item[1]==1:
                print(item[0])
                flag = True
                break
            else:
                pass
        # if 1 not in l.values():
        #     print(-1)

        if flag == False:
            print(-1)
    except:
        break
