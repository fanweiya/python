from random import randint
List = [randint(-10, 10000) for _ in range(10)]  # 生成10个-10到100之间的随机数字
for Index in range(1, len(List)):
    I = Index  # 刚开始往左边走的第一个位置
    val = List[I]  # 先把当前值存起来
    while I > 0 and val < List[I - 1]:
        List[I] = List[I - 1]
        I -= 1
    List[I] = val
print(List)
