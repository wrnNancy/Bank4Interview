# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: listnode.py
@Author: wuruonan
@Create: 6/20/22 3:52 下午 
@Description:链表节点定义
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None