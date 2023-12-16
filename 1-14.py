##c=0
##for i in range(1,5):
##    for j in range(1,5):
##        for k in range(1,5):
##            if i!=j and i!=k and j!=k:
##                print(i,j,k)
##                c+=1
##print(c)

y=int(input("year:"))
m=int(input("month:"))
d=int(input("day:"))
if y%4==0 and y%100!=0 or y%400==0:
    list=[0,31,60,91,121,152,182,213,244,274,305,335]
else:
    list=[0,31,59,90,120,151,181,212,243,273,304,334]
i=list[m-1]+d
print(m,"月",d,"日","是",y,"年的第",i,"天")
    
