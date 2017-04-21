from random import randint
li = [randint(-10, 1000) for _ in range(10)]  # 生成10个-10到100之间的随机数字
for n in range(len(li)):  # 循环列表中所有的元素
    for i in range(len(li) - 1 - n):  # 每次求最大值，放到最后，不对比匹配到最大的那个值
        if li[i] > li[i + 1]:  # 当前值大于当前值的下一个
            li[i], li[i + 1] = li[i + 1], li[i]  # 位置调换一下
print(li)  # 输出