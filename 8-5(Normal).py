##u=lambda x:print("偶数") if x%2==0 else print("奇数 ")
##N=int(input("num:"))
##u(N)

##def dgcf(n,m):
##    if m==1:
##        return n
##    else:
##        return n*dgcf(n,m-1)
        
##def fbnq(n):
##    if n<3:
##        return 2 
##    else:
##        return fbnq(n-1)+fbnq(n-2)

def fbnq(n):
    if n==10:
        return 1
    else:
        return (fbnq(n+1))*2
for i in range(10):
    fbnq(i)
