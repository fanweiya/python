#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from random import randint
li = [randint(-20, 100) for _ in range(10)]
def quick_sort(List, start, end):
    print(List, start, end)
    if start >= end:
        return
    Key = List[start]  # 值
    LeftIndex = start  # 左边
    RightIndex = end  # 右边
    while LeftIndex < RightIndex:  #
        while LeftIndex < RightIndex and List[RightIndex] > Key:  # 代表要继续往左边移动小旗子
            RightIndex -= 1
        List[LeftIndex], List[RightIndex] = List[RightIndex], List[LeftIndex]
        while LeftIndex < RightIndex and List[LeftIndex] <= Key:  # 左边小旗子开始向右移动
            LeftIndex += 1
        List[LeftIndex], List[RightIndex] = List[RightIndex], List[LeftIndex]
    quick_sort(List, start, LeftIndex - 1)  # 左边
    quick_sort(List, LeftIndex + 1, end)
quick_sort(li, 0, len(li) - 1)
print(li)