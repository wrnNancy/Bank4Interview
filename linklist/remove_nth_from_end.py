# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: remove_nth_from_end.py
@Author: wuruonan
@Create: 6/20/22 8:06 下午 
@Description:删除链表的倒数第n个节点
"""

"""题目内容：
给定一个链表，删除链表的倒数第 n 个节点并返回链表的头指针
例如，
给出的链表为:1→2→3→4→5,n=2.
删除了链表的倒数第 n 个节点之后,链表变为1→2→3→5.

数据范围： 链表长度  0≤n≤1000，链表中任意节点的值满足 0≤val≤100
要求：空间复杂度 O(1)，时间复杂度 O(n)
备注：
题目保证 n 一定是有效的
"""
from linklist.listnode import ListNode


class RemoveNthFromEnd:
    def __init__(self):
        pass

    def double_link(self, head:ListNode, n:int) -> ListNode:
        if not head:
            # 链表为空的处理
            return
        slow = head
        fast = head
        for i in range(0, n):
            fast = fast.next
        if not fast:
            # 要删除的节点为边界节点时的处理，n>=len
            return head.next

        while fast.next:
            # 快慢指针同时前进
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        # 删除慢节点
        return head
