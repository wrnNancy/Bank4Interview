# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: delete_duplicates_1.py
@Author: wuruonan
@Create: 6/20/22 8:31 下午 
@Description: 删除有序链表中重复元素-1
"""

"""题目内容：
删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
例如：
给出的链表为1→1→2,返回1→2.
给出的链表为1→1→2→3→3,返回1→2→3.

数据范围：链表长度满足 00≤n≤100，链表中任意节点的值满足 0∣val∣≤100
进阶：空间复杂度 O(1)，时间复杂度 O(n)
"""
from linklist.listnode import ListNode


class DeleteDuplicates1:
    def double_points(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        q = head.next
        while p and q:
            if p.val != q.val:
                p = p.next
                q = q.next
            else:
                while p and q and p.val == q.val:
                    q = q.next
                p.next = q
        return head