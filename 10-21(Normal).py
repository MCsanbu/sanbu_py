list=[1,2,3]
num=0
while num<1200:
    l=len(list)
    num=(list[l-3]+list[l-2]+list[l-1])//2
    list.append(num)
print(l)
