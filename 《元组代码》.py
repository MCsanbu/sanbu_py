a=(1,2,3,4)
b=(5,6,7)
c=[1,2,3]
print(len(a)) #计算元素个数

print(a+b)#连接元组

d=tuple(c)
print(type(d))#列表变元组

e=a*4
print(e) #复制元组

del a
print(a) #删除整个元组

