def sblox(l):
    for y in range(b):
        for x in range(a-1):
            if l[x][y]!="#" and l[x][y]!="-":
                if l[x+1][y]=="-":
                    l[x+1][y]=l[x][y]
                    l[x][y]="-"
    return l
def rep(l,x,y,t):
    old=l[x][y]
    for xy in range(4):
        if l[x+dx[xy]][y+dy[xy]]==old or l[x+dx[xy]][y+dy[xy]]==t:
            l[x+dx[xy]][y+dy[xy]]=t
            l[x][y]=t
    return l

def l2hyp(l,t):
    c=0
    for i in range(a):
        for y in range(b):
            if l[i][y]==t:
                c+=1
                l[i][y]='-'
    return l,c

def loopch(l):
    for y in range(b):
        for x in range(a):
            if l[x][y]=="A":
                l=rep(l,x,y,'1')
            elif l[x][y]=="B":
                l=rep(l,x,y,'2')
            elif l[x][y]=="C":
                l=rep(l,x,y,'3')
    return l
a,b=[int(x) for x in input().split()]
l=[]
for i in range(a):
    x=input().split()
    l.append(x)
c=0   
n=int(input())
for i in range(n):
    x,y,di=input().split()
    x,y=int(x),int(y)
    floppa=l[x][y]
    cc=0
    if di=="L":
        cc=-1
    else:
        cc=1

    ch=0
    if l[x][y+cc]=="-" and l[x][y] in 'ABC':
        l[x][y+cc]=l[x][y]
        l[x][y]="-"
    else:
        c-=5
    l=sblox(l)
    old=''
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    score=0
    for i in range(2):
        l=loopch(l)
        l=sblox(l)
        l,score=l2hyp(l,'1')
        l=sblox(l)
        c+=score*5
        l,score=l2hyp(l,'2')
        l=sblox(l)
        c+=score*5
        l,score=l2hyp(l,'3')
        l=sblox(l)
        c+=score*5
print(c)                 
for i in l:
    for y in i:
        print(y,end=" ")
    print("")