# -*- coding: utf-8 -*-
# @Time : 2021/11/4 2:48 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : deleteAaA.py

class Solution:
    """
    AaA 意思就是删除字符串中的所有驼峰字符串
    输入：AaAabcdfAAaAaA 输出：abcdef
    """

    def deletAaA(s):
        # 首先判断字符串的长度
        if len(s) <= 2:
            return []
        res = []
        for i in range(len(s) + 1):
            # 长度大于2就可能出现驼峰
            if len(res) > 2:
                # 出现驼峰
                if res[-1] == res[-3] and res[-1].isupper() and res[-2].islower():
                    # 删除
                    del res[-3:]
            if i < len(s):
                res.append(s[i])
        return ''.join(res)


if __name__ == '__main__':
    print(Solution.deletAaA('AhfhdjhsAAjhdshdjsAAyg'))
