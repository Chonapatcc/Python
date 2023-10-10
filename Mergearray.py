n=int(input())
l1=[]
l2=[]
for i in range(n):
    a=list(map(int,input().split()))
    l1.append(a)
for i in range(n):
    a=list(map(int,input().split()))
    l2.append(a)
way=input()
posi=int(input())

if way=="H":
    for i in range(n):
        pos=posi-n
        l=[]
        
        if pos>=1:
            pos-=1
            l=[0]*pos
            l1[i]=l1[i][:posi]+l+l2[i]+l1[i][posi:]
        else:
            co=0
            for y in range(posi-1,posi+n-1):
                if y>=n:
                    l1[i].append(l2[i][co])
                    co+=1
                else:
                    l1[i][y]+=l2[i][co]
                    co+=1

else:
    co=0
    pos=posi-n
    l=[]
    if pos>1:
        pos-=1
        for i in range(pos):
            l1.append([0]*n)
    for i in range(posi-1,posi+3-1):
        if posi<=n:
            if i<=n-1:

                for y in range(n):
                    l1[i][y]+=l2[co][y]
                co+=1
            else:
                l1.append(l2[co])
                co+=1
        else:
            l1.append(l2[co])
            co+=1
for i in l1:
    for y in i:
        print(y,end=' ')
    print()
            
        
        