def recur(old,new):
    l=[]
    for i in old:
        for y in new:
            if i[-1]==y[0]:
                l.append([i[0],y[-1]])
    return l
    

n,p=[int(x) for x in input().split()]
l=[[] for x in range(n)]
for i in range(p):
    a,b=[int(x) for x in input().split()]
    x=[]
    if a>b:
        x=[b,a]
    else:
        x=[a,b]
    l[x[0]-1].append(x)
nl=[]
for i in range(len(l)-1):
    for y in range(len(l[i])):
        old=l[i][y]
        lnew=l[l[i][y][-1]-1]
        for x in lnew:
            nl.append([old,x])
print(l)
print(nl)
        