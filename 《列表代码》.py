list=["a","b","c","d",1,2.2]
list[-1]="e"#列表的修改
print(list)
bo="a"in list #列表的查找
print(bo)
print(list.index("e"))#列表下标查找
print(list.count("a"))#列表元素出现的个数
del list[-1]#列表删除元素用索引
print(list)
list.pop(0)#列表删除元素返回删除的元素
print(list)
list.remove("d")#列表删除元素如果有相同的元素从左到右依次删除
print(list)
list.append("z")#列表的增加
print(list)
list2=list[::]
print(list2)
print(list[::-1])#从后往前输出
##list.sort()#列表排序排的是int类型,注：可用reverse=True
list.insert(3,6)#插入元素至列表
print(list)
##max(list)#列表中最大的元素
##min(list)#列表中最小的元素
list3=[7,8,9]
list4=[3,4]
list3.extend(list4)#插入别的列表
print(list3)
list5=['google','copilot','baidu','sanbu']
list5.reverse()#反转
print(list5)
#1.输入3个，添加至列表
a=input("a:")
b=input("b:")
c=input("c:")
list6=[]
list6.append(a)
list6.append(b)
list6.append(c)
print(list6)

#2.随机3个数，添至列表并排序
import random
list7=[]
for i in range(3):
    a=random.randint(0,100000)
    list7.append(a)
    list7.sort(reverse=False)
print(list7)
    




