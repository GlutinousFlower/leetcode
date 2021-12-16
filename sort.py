# -*- coding: utf-8 -*-
# @Time : 2021/10/18 2:57 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : sort.py

def bubble_sort(list):
    length = len(list)
    for index in range(length):
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list


def quick_sort(list):
    pivotList = []
    less = []
    more = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivotList + more


def selection_sort(list):
    n = len(list)
    for i in range(1, n):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
                list[min], list[i] = list[i], list[min]
    return list

def merge_list(list1,list2):
    #list1和list2是长度相同的有序数组，将其合并
    counta=0
    countb=0
    c=[]
    for i in range(counta,len(list1)):
        for j in range(countb,len(list2)):
            if list2[j]<=list1[i]:
                c.append(list2[j])
                countb=countb+1
            else:
                c.append(list1[i])
                counta=counta+1
                break

    if counta<len(list1):
        for i in range(counta,len(list1)):
            c.append(list1[i])
    if countb<len(list2):
        for j in range(countb,len(list2)):
            c.append(list2[j])
    return c

if __name__ == '__main__':
    print(merge_list([1,2,5,8,9],[0,2,4,6,8,9]))











