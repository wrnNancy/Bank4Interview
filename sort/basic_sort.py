# coding=utf-8
# !/usr/bin/env python
# -*- coding :utf-8 -*-
# Authors: wrnNancy
# 2021-03-30
"""
:description:
    基础的八种排序算法
"""


class BasicSort(object):
    """ 基础排序类 """

    def __init__(self):
        """
            初始化
        """
        pass

    @classmethod
    def straight_insert_sort(cls, unsort_list):
        """
            直接插入排序,传入对象为list
            1. 原理：分为有序区与无序区，每次从无序区中选择一个值插入到有序区
            2. 空间复杂度：O(1)——需要一个temp做中间转换
            3. 时间复杂度：最优-；最差-
        """
        print 'basic list is {0}'.format(unsort_list)
        for i in range(1, len(unsort_list)):
            current = i
            for j in range(0, i):
                if unsort_list[current] < unsort_list[j]:
                    temp = unsort_list[j]
                    unsort_list[j] = unsort_list[current]
                    unsort_list[current] = temp
            print 'after {0} time sorted, list is {1}'.format(i, unsort_list)
        return unsort_list

    @classmethod
    def selection_sort(cls, unsort_list):
        """选择排序"""
        print 'basic list is {0}'.format(unsort_list)
        for i in range(0, len(unsort_list)):
            current = i
            j = i + 1
            while j < len(unsort_list):
                if unsort_list[j] < unsort_list[current]:
                    current = j
                j = j + 1
            if current != i:
                temp = unsort_list[i]
                unsort_list[i] = unsort_list[current]
                unsort_list[current] = temp
            print 'after {0} time sorted, list is {1}'.format(i, unsort_list)
        return unsort_list


if __name__ == '__main__':
    test_sort = BasicSort()
    test_list_sorted = [1, 2, 3, 4, 5, 6, 7]
    test_list_desorted = [7, 6, 5, 4, 3, 2, 1]
    test_list_unsorted = [3, 2, 4, 6, 7, 5, 1]
    print test_sort.selection_sort(test_list_sorted)
    print test_sort.selection_sort(test_list_desorted)
    print test_sort.selection_sort(test_list_unsorted)
