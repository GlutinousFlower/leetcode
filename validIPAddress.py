# -*- coding: utf-8 -*-
# @Time : 2021/11/17 4:18 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : validIPAddress.py
import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        list_ip = IP.split('.')
        for i in list_ip:
            if re.match("^[1-9]", i)==None:
                return "Neither"
            elif 0 <= int(i) <= 255:
                    return "IPv4"


if __name__ == '__main__':
    print(Solution().validIPAddress("10.5.1.23"))
