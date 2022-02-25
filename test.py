# -*- coding: utf-8 -*-
# @Time : 2022/2/14 6:49 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : test.py

def test(s1,s2):
    s=set(s1)
    print(s)

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                print(s1[i],s1.count(s1[i])+s2.count(s2[j]))


if __name__ == '__main__':
    test('hello','hely')
