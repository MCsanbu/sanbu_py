a=int(input("num:"))
for i in range(a):
    for j in range(a-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print("")    
for i in range(a):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(a-i)-1):
        print("*", end=" ")
    print("")
