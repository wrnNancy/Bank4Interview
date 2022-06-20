# !/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@File: merge_2_sorted_list.py
@Author: wuruonan
@Create: 6/20/22 3:04 下午 
@Description: 合并两个有序数组
"""

"""题目内容：
给出一个整数数组  A 和有序的整数数组  B ，请将数组  B 合并到数组  A 中，变成一个有序的升序数组
注意：
1.可以假设  A 数组有足够的空间存放  B数组的元素，  A 和  B 中初始的元素数目分别为  m 和  n ， A 的数组空间大小为  m +  n 
2.不要返回合并的数组，返回是空的，将数组  B 的数据合并到 A 里面就好了
3. A 数组在[0,m-1]的范围也是有序的

例1:
A: [1,2,3,0,0,0]，m=3
B: [2,5,6]，n=3
合并过后A为:
A: [1,2,2,3,5,6]
"""


class Solution:
    def __init__(self):
        pass

    def merge(self, A, m, B, n):
        # write code here
        if m == 0:
            A[:] = B[:]
            return A
        if n == 0:
            return A
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0 and k >= 0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i = i-1
            else:
                A[k] = B[j]
                j = j-1
            k = k-1

        if k >= 0 and j >= 0:
            for p in range(0, j+1):
                A[p] = B[p]
                # A[0:k] = B[0:j] ----- k为0时，取值为空
            # ---- 剩余为A时，无需处理
        return A


if __name__ == '__main__':
    temp_class = Solution()
    A = [2, 0]
    m = 1
    B = [1]
    n = 1
    res = temp_class.merge(A, m, B, n)
    print(res)


