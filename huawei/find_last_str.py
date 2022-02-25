# -*- coding: utf-8 -*-
# @Time : 2022/1/10 8:42 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : find_last_str.py
#
# while True:
#     try:
#         s=input()
#         arr=s.split(' ')
#         print(len(arr[-1]))
#
#     except:
#         break

def zhishu(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


def fenjie(num):
    while num > 1:
        for i in range(2, num + 1):
            if zhishu(i) and (num % i == 0):
                num //= i
                print(i)
                break


if __name__ == '__main__':
    # print(zhishu(4))
    fenjie(180)
    # print(5 % 3)
