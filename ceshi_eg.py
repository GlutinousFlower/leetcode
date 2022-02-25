# -*- coding: utf-8 -*-
# @Time : 2022/1/12 2:08 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : ceshi_eg.py

# 不带参数的函数装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)

    return wrapper


@decorator
def bar():
    print('foo')


bar()


# 带参数的函数装饰器
def hello(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('hello')
            return func(*args, **kwargs)

        return wrapper

    return decorator


@hello('test1')
def test():
    print('test2')


test()


# 类装饰器

class Demo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('class')
        return self.func(*args, **kwargs)


@Demo
def class_test():
    print('test class')


class_test()


# 内置函数
# @property
# 特性装饰器（作用于类里的函数，使得我们像访问类属性一样获取函数返回值）
# @staticmethod
# 静态方法装饰器（同样作用于类里的函数，表示是一个静态函数，可以直接通过类名调用该方法，无需实例化，但是意味着没有self参数）
# @classmethod
# 类方法装饰器（同静态方法一致，不同的是，会接受一个指向类本身的cls参数）
