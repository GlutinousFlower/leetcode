# -*- coding: utf-8 -*-
# @Time : 2021/11/8 4:01 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : pythonPoint.py

class A:
    pass


class B(A):
    pass


class C(B):
    def test(self):
        print('c')


class E:
    def test(self):
        print("e")


class F(E):
    pass


class G(F):
    pass


class H(C, G):
    pass


if __name__ == '__main__':
    H().test()
