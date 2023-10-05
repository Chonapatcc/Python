n=int(input())
l=[]
c=0
for i in range(n):
    x=input()
    if x!="Q":
        a,b=x.split()
        l.append(int(b))
        c+=1
    else:
        if c==0:
            print(-1)
        else:
            l.sort()
            c-=1
            print(l.pop())



