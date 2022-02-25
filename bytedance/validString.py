# -*- coding: utf-8 -*-
# @Time : 2021/10/11 3:45 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : validString.py

"""
括号匹配
"""


class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
