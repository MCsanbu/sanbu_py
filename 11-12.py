
def my_abs(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    return my_abs(n-1)+my_abs(n-2)
for i in range(10):
    print(my_abs(i))
    
    
