def filter_sort_factors_3_7(ls):
    l1=[]
    l2=[]
    for i in ls:
        if i>0:
            if i%3==0 or i%7==0:
                l1.append(i)
            else:
                l2.append(i)
    l1.sort()
    l2.sort(reverse=True)
    return [l1,l2]
print(filter_sort_factors_3_7(list(range(-100,10))))
