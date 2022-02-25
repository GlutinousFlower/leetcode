# -*- coding: utf-8 -*-
# @Time : 2022/1/6 3:21 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : count_factor.py

def count_factor():
    # 求一个自然数的所有因子 - - Python
    # 问题分析 ：从1到n,依次对n取余，如果这个数是它的因子，则保留。
    # 然后对 n，i, 更新重新此过程，直到结束（不考虑重复添加情况）。
    # 功能: 输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2,2,3,3,5 ）


    n=int(input())
    if n == 0: return [0]
    if n <= 3: return [1]

    tmp = n
    rlist = []
    i = 2
    while i <= tmp:
        if tmp % i == 0:
            rlist.append(i)
            tmp = tmp // i
            i = 2
            continue
        i += 1
    for j in range(len(rlist)):
        print(rlist[j])


if __name__ == '__main__':
    count_factor()


