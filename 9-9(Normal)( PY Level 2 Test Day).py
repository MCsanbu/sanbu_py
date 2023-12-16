def quicksort(list):
    if len(list)<2:
        return list
    mid=list[len(list)//2]
    left,right=[],[]
    list.remove(mid)
    for i in list:
        if i>=mid:
            right.append(i)
        else:
            left.append(i)
    return quicksort(left)+[mid]+quicksort(right)
