# -*- coding: utf-8 -*-
# @Time : 2021/8/31 11:39 上午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : lengthOfLongestSubstring.py

"""
最长不重复子串
"""


class LengthOfLongestSubstring:
    def lengthOfLongestSubstring(self, s):
        l = []
        length = []
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        else:
            for i in range(len(s)):
                # print(s[i:])
                for f in s[i:]:
                    if f in l:
                        length.append(len(l))
                        l.clear()
                        break
                    else:
                        l.append(f)
            return max(length, default=0)


if __name__ == '__main__':
    # print(len(' '))
    print(LengthOfLongestSubstring().lengthOfLongestSubstring('cdhbjhsbjsc'))
    # 需要考虑下兜底，s=''和s=' ','a'这种情况，以及l被清空后的length值，给一个default
