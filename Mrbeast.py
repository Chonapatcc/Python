def find(t1,t2,l):
    
    t2+=1
    if t2 not in d:
        d[t2]=l
    if t1==t2:
        return l
    else:
        
        return find(t1,t2,l)


n=[int(x) for x in input().split()[:-1]]

for i in n:
    l=[1,1,0]
    for y in range(i):
        x,y,z=l
        y,z=y+1+z,y
        l=[x,y,z]
    print(l[1],sum(l))
