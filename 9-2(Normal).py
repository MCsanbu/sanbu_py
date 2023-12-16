##def inser(list):
##    for i in range(1,len(list)):
##        a=list[1]
##        j=i-1
##        while j>=0 and a<list[j]:
##            list[j+1]=list[j]
##            j-=1
##        list[j+1]=a
##arr=[]
##inser(arr)
##print(arr)

def inser2(list):
    if len(list)<=1:
        return list
    for right in range(1,len(list)):
        a=list[right]
        for left in range(0,right):
            if a<=list[left]:
                list[left+1:right+1]=list[left:right]
                list[left]=a
                break
    return list
