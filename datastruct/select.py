from random import randint
List = [randint(-10, 1000) for _ in range(10)]  # 生成10个-10到100之间的随机数字
for Index in range(len(List)):  # 循环列表所有索引
    Sam = Index  # 最小值的索引
    for I in range(Index, len(List)):  # 每次循环都不取上次取到的最大值
        if List[Sam] > List[I]:  # 列表的某个值大于当前小循环的值
            Sam = I  # 最小值的所以赋值给sma
    List[Index], List[Sam] = List[Sam], List[Index]  # 交换位置
print(List)