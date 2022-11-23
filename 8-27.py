a=int(input("num:"))
b=0
for i in range(a+1):
    if i%2==0:
       b -= i*i
    else:
        b+=i*i
print(b)
