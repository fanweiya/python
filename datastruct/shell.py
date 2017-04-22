from random import randint
List = [randint(-20, 100) for _ in range(10)]  # 生成10个-10到100之间的随机数字
Step = int(len(List) / 2)  # 将列表切分成两半
while Step >= 1:  # 如果切分的值大于等于1
    for Index in range(len(List) - Step):
        if List[Index] > List[Index + Step]:
            List[Index], List[Index + Step] = List[Index + Step], List[Index]  # 位置交换
    Step = int(Step / 2)
else:  # 进入插入排序
    for Index in range(len(List)):
        while Index > 0 and List[Index] < List[Index - 1]:
            List[Index], List[Index - 1] = List[Index - 1], List[Index]
            Index -= 1
print(List)