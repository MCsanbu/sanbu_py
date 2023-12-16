n=int(input("num:"))
m=int(input("num:"))
m-=1
k=int(input("num:"))
a=0
list=[]
list2=[]
index=k-1
for i in range(1,n+1):
    list.append(i)
while len(list)>1:
    index=(index+m-1)%len(list)
    a=list.pop(index)
    list2.append(a)
last=list[0]
print(last,list2)
    
