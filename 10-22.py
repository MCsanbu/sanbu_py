for x in range(10):
    a=int(input("num:"))
    for i in range(1,a+1):
        for j in range(a-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*",end=" ")
        print("\n")    
    for i in range(1,a+1):
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*(a-i)-1):
            print("*", end=" ")
        print("\n")
