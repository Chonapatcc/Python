n=int(input())
l=[]
lc=[0]*n
s=-1
ch=False
l2r=0
r2l=0
c2=0
m=-50
nm=100
for i in range(n):
    if ch:
        break
    x=[int(x) for x in input().split()]
    if s==-1:
        s=sum(x)
    else:
        if s!=sum(x):
            ch=True
    for ind in range(n):
        lc[ind]+=x[ind]
    l.append(x)
    l2r+=x[c2]
    r2l+=x[-(c2+1)]
    c2+=1
    mm=max(x)
    nn=min(x)
    if mm>m:
        m=mm
    if nn<nm:
        nm=nn
if m>n**2 or m<1 or m!=n**2:
    ch=True
if nm>n**2 or nm<1 or nm!=1:
    ch=True
if lc.count(s)!=n:
    ch=True

if l2r!=r2l or l2r!=s or r2l!=s:
    ch=True

if ch:
    print('No')
else:
    print('Yes')


    