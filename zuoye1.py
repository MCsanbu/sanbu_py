c=0
for i in range(1800,3000):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)
        c+=1
print(c)

        
