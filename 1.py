m=int(input("money:"))
t=int(input("time:"))
l=float(input("年利率:"))
n=int(input("n:"))
we=0
co=0
a=m*0.7
b=a//t//12
bt=t*12
c=l/12
for i in range(0,bt):
    we=(a-i*b)*c+b
    co+=we-b
print(co+m)  
    
    
