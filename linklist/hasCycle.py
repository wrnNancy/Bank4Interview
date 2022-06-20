# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: hasCycle.py
@Author: wuruonan
@Create: 6/20/22 3:50 下午 
@Description: 判断链表是否有环
"""

"""题目描述：
判断给定的链表中是否有环。如果有环则返回true，否则返回false。

数据范围：链表长度 0≤n≤10000，链表中任意节点的值满足 |val| <= 100000
要求：空间复杂度 O(1)，时间复杂度 O(n)

输入分为两部分，第一部分为链表，第二部分代表是否有环，然后将组成的head头结点传入到函数里面。
-1代表无环，其它的数字代表有环，这些参数解释仅仅是为了方便读者自测调试。实际在编程时读入的是链表的头节点。

例如输入{3,2,0,-4},1时，对应的链表结构如下图所示：
3-->2-->0--->4
    ｜       ｜
    <---------
可以看出环的入口结点为从头结点开始的第1个结点（注：头结点为第0个结点），所以输出true。
"""

from linklist.listnode import ListNode

class HasCycle:
    def __init__(self):
        pass

    def double_point(self, head: ListNode) -> bool:
        # 快慢指针
        if not head or not head.next:
            return False
        fast_node = head
        slow_node = head
        while slow_node and fast_node:
            slow_node = slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                return False
            if slow_node == fast_node:
                return True
        return False

    def hash_table(self, head: ListNode) -> bool:
        # 哈希表--字典/python不建议
        if not head or not head.next:
            return False
        res_dict = {}
        while head:
            if head not in res_dict:
                res_dict[head] = True
                head = head.next
            else:
                return True
        return False

    def hash_table_list(self, head: ListNode) -> bool:
        # 哈希表--列表/python不建议
        if not head or not head.next:
            return False
        res_list = []
        while head:
            if head not in res_list:
                res_list.append(head)
                head = head.next
            else:
                return True
        return False


