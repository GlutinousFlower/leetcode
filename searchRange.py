# -*- coding: utf-8 -*-
# @Time : 2021/10/11 4:44 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : searchRange.py
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        result = []
        if target not in nums:
            return [-1, -1]
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    l.append(i)
                    continue
                if i > target:
                    break
            if len(l) == 1:
                l.append(l[0])
        print(l)
        return l


if __name__ == '__main__':
    Solution().searchRange([0,0,2,3,4,4,4,5], 5)
