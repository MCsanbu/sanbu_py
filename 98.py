##a=1
##sum=0
##
##for i in range(1,11):
##    a*=i
##    
##    sum+=a
##print(sum)
##    

##for i in range(1,5,1):
##    for k in range(1,5,1):
##        for j in range(1,5,1):
##          if i != k and i != j and k != j:
##              c=(i)*100 +(k)*10 +(j) 
##print(c)

for i in range(100,1000):
    a=i//100
    b=i%100//10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)
    
  
