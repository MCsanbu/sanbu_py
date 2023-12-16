##o=[i**2 for i in range(10) if i%2!=0]
##print(o)
sum=0
y=int(input("year:"))
m=int(input("month:"))
d=int(input("day:"))
list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
list2=[0,31,29,31,30,31,30,31,31,30,31,30,31]
if y%4==0 and y%100!=0 or y%400==0:
    for i in range(m):
        sum+=list2[i]
    sum=sum+d
else:
    for i in range(m):
        sum+=list[i]
    sum=sum+d
print(sum)

