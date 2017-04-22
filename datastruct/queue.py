#!/use/bin/env python
# _*_ coding:utf-8 _*_
from collections import deque
def yanghui(k):
    """
    :param k: 杨辉三角中第几层
    :return: 第K层的系数
    """
    q = deque([1])  # 创建一个队列，默认从1开始
    for i in range(k):  # 迭代要查找的层数
        for _ in range(i):  # 循环需要出队多少次
            q.append(q.popleft() + q[0])  # 第一个数加上队列中第二个数并赋值到队列末尾
        q.append(1)  # 每次查找结束后都需要在队列最右边添加个1
    return list(q)
result = yanghui(3)
print(result)


#!/use/bin/env python
# _*_ coding:utf-8 _*_
from collections import deque
def division(m, n):
    """
    :param m: 冲突关系矩阵
    :param n: 几种动物
    :return: 返回一个栈，栈内包含了所有的笼子
    """
    res = []  # 创建一个栈
    q = deque(range(n))  # 初始化队列，里面放着动物的序号
    pre = n  # 前一个动物的下标
    while q:
        cur = q.popleft()  # 从队头出队一个动物
        if pre >= cur:  # 是否需要创建笼子
            res.append([])  # 创建一个笼子
        # 当前的动物是否与笼子内的动物有冲突
        for a in res[-1]:  # 迭代栈中最顶层的笼子
            if m[cur][a]:  # 有冲突
                q.append(cur)  # 重新放入队列的尾部
                break
        else:  # 当前动物和当前笼子中的所有动物没冲突
            res[-1].append(cur)  # 当前动物放入最上面的笼子中
        pre = cur  # 当前变成之前的
    return res
N = 9
R = {  # 冲突对应关系表
    (1, 4), (4, 8), (1, 8), (1, 7),
    (8, 3), (1, 0), (0, 5), (1, 5),
    (3, 4), (5, 6), (5, 2), (6, 2), (6, 4),
}
M = [[0] * N for _ in range(N)]  # 冲洗关系矩阵M，0代表不冲突
for i, j in R:
    M[i][j] = M[j][i] = 1  # 1代表冲突
result = division(M, N)
print(result)


from collections import deque
def atob(a, b):
    """
    :param a: 开始的数字
    :param b: 最终转换之后的数字
    :return: 最小匹配的次数
    """
    q = deque([(a, 0)])  # a=当前数字，0=操作的次数
    checked = {a}  # 已经检查过的数据
    while True:
        s, c = q.popleft()
        if s == b:
            break
        if s < b:  # 要计算的数小于计算之后的数字
            if s + 1 not in checked:  # 如果要计算的数字+1不在已检查过的数据集合中
                q.append((s + 1, c + 1))  # 要计算的数+1，转换次数+1
                checked.add(s + 1)  # 把计算过的数添加到checked集合中
            if s * 2 not in checked:
                q.append((s * 2, c + 1))
                checked.add(s * 2)
        if s > 0:  # 要计算的数大于0
            if s - 1 not in checked:
                q.append((s - 1, c + 1))
                checked.add(s - 1)
    return q.popleft()[-1]
result = atob(3, 11)
print(result)