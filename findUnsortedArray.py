# -*- coding: utf-8 -*-
# @Time : 2021/11/2 3:27 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : findUnsortedArray.py
from typing import List


class Solution:
    """
    输入：nums = [2,6,4,8,10,9,15]
    输出：5
    解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2 and sorted_nums[p1] == nums[p1]:
            p1 += 1
        while p1 <= p2 and sorted_nums[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([1,2,3,5,6,9,8]))