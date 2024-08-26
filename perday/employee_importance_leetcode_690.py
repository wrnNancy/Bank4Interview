#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 19:16
# @Author  : wu ruonan
# @File    : employee_importance_leetcode_690.py
# @Software: PyCharm


"""题目内容：690. 员工的重要性
题目链接：https://leetcode.cn/problems/employee-importance/description/
你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。

给定一个员工数组 employees，其中：

employees[i].id 是第 i 个员工的 ID。
employees[i].importance 是第 i 个员工的重要度。
employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。
给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。

示例 1：
输入：employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
输出：11
解释：
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。


示例 2：
输入：employees = [[1,2,[5]],[5,-3,[]]], id = 5
输出：-3
解释：员工 5 的重要度为 -3 并且没有直接下属。
因此，员工 5 的总重要度为 -3。
"""
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:

    def getImportance(cls, employees: List['Employee'], id: int) -> int:
        """解法分析：
        首先，创建一个哈希表，把第 i 个员工的 ID 映射到 employees[i] 对象上。

        然后从 id 开始 DFS（题目保证员工组成了树形结构）：

        根据 id 从哈希表中获取到对应的员工对象 e。
        把 e.importance 加到返回值中。
        遍历 e.subordinates，继续 DFS 下属的 ID，把 dfs(subId) 加到返回值中。

        时间复杂度：n，emloyees的长度；每个员工至多访问一次
        空间复杂度：n
        """
        employees = {e.id: e for e in employees}
        # 字典推导式，将员工id映射到哈希表中；可通过员工编号得到对应员工

        def dfs(idx: int) -> int:
            e = employees[idx]
            return e.importance + sum(dfs(subIdx) for subIdx in e.subordinates)
            # 深度优先遍历的递归解法
        return dfs(id)


if __name__ == '__main__':
    templist = [
        Employee(1, 5, [2, 3]),
        Employee(2, 3, []),
        Employee(3, 3, [])]
    print(Solution().getImportance(templist, 1))


