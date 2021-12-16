# -*- coding: utf-8 -*-
# @Time : 2021/9/30 2:34 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : powerOfThree.py
'''
判断某个数是不是3的幂
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''递归法'''
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


    def isPowerOfThree02(self, n: int) -> bool:
        '''试除法'''
        while n and n % 3 == 0:
            n = n // 3

        return n == 1


if __name__ == '__main__':
    Solution().isPowerOfThree02(8)
