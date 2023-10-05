w,h,n=[int(x) for x in input().split()]

l=[0]*(w)
for i in range(n):
    a,b=[int(x) for x in input().split()]
    for i in range(a,a+b):
        if i <w:
            l[i]+=1
p50=l.count(1)*h
p100=l.count(0)*h
print(p100,p50)
