grade={"m":90,"c":97,"e":92,"z":90}

#查
print(grade.get("e"))#用键查值
print(grade.keys())#获取字典中所有的键
print(grade.values())#获取字典中所有的值

#增&改
grade.update({"p":100})#字典添加1
grade.update({'m':100})#字典更改1
grade.update(w=99)#字典添加2
grade.update(m=80)#字典更改2
grade['s']=93#字典添加3
grade['c']=88#字典更改3

#删
print(grade.pop('z'))#删除指定的键值对 并返回该值
print(grade.popitem())#默认删除最后一个键值对 并返回该值
del grade['m']#删除指定的键值对
##grade.clear()#清除字典中所有的键值对
##print(grade)
##del grade#删除整个字典
##print(grade)

#遍历
for i in grade.keys(): #遍历字典的键
    print(i)
for i in grade.values(): #遍历字典的值
    print(i)
for i in grade.items(): #遍历字典的键值对
    print(i)
    print(type(i))
for i,j in grade.items(): #遍历字典的键值对
    print(i,j)


