# -*- coding: utf-8 -*-
# @Time : 2021/9/17 3:30 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : longestCommonSubsequence.py
"""
最长重复子串
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l = []
        index = []
        if text1 == '' or text2 == '':
            return 0
        else:
            for i in text1:
                if i in text2:
                    l.append(i)
                    index.append(text2.index(i))
                    continue
            for j in range(len(index) - 1):
                if index[j] >= index[j + 1]:
                    l = l[:j + 1]
        # print(l, index)
        return len(l)


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence(text1="bsbininm", text2='jmjkbkjkv'))
