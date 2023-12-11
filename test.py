def max_sequence(arr):
    if len(arr)==0:
        return 0
    l=[]
    le=len(arr)
    for i in range(le):
        for y in range(le+1):
            a1=(arr[i:i+y])
            a2=arr[i+y:le]
            a3=arr[i+y:le-y]
            #print(a1,a2,a3)
            la=[a1,a2,a3]
            for item in la:
                if len(item)>0:
                    l.append(sum(item))


    m=max(l)
    #print(m)
    
    return m
        
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))