# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: entry_of_loop.py
@Author: wuruonan
@Create: 6/20/22 4:12 下午 
@Description: 链表中环的入口节点
"""

"""题目内容：
给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。

数据范围： 0n≤10000，1<=结点值<=10000
要求：空间复杂度 O(1)，时间复杂度 O(n)

例如，输入{1,2},{3,4,5}时，对应的环形链表如下图所示：
1 --> 2 ---> 3 ----->4
             |       |
             <---5<---
可以看到环的入口结点的结点值为3，所以返回结点值为3的结点。
输入描述：
输入分为2段，第一段是入环前的链表部分，第二段是链表环的部分，后台会根据第二段是否为空将这两段组装成一个无环或者有环单链表
返回值描述：
返回链表的环的入口结点即可，我们后台程序会打印这个结点对应的结点值；若没有，则返回对应编程语言的空结点即可。
"""


from linklist.listnode import ListNode


class EntryOfLoop:
    def __init__(self):
        pass

    def double_point(self, pHead: ListNode):
        if not pHead or not pHead.next:
            return
        slow_node = pHead
        fast_node = pHead
        while slow_node and fast_node:
            slow_node = slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                return
            if slow_node == fast_node:
                break
        if not fast_node or not fast_node.next:
            return
        # 以上同链表是否有环

        fast_node = pHead
        # 指针分别放在头节点、当前节点，走环的长度，相遇即入口
        while slow_node != fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
        return slow_node

    def hash_table(self, pHead: ListNode):
        # 哈希表，字典
        res_dict = {}
        while pHead:
            if pHead not in res_dict:
                res_dict[pHead] = True
                pHead = pHead.next
            else:
                return pHead
        return
