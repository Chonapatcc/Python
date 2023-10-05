
#case 8 n=6 but n-1
def func(y,x,l):
    pt=l[y][x]
    s=[[y,x]]
    c=0
    for i in range(4):
        if y+dyl[i]<n and y+dyl[i]>=0 and x+dxl[i]<n and x+dxl[i]>=0:
            if pt==l[y+dyl[i]][x+dxl[i]]:
                c+=1
                s.append([y+dyl[i],x+dxl[i]])
    if c==2:
        ch=False
        c1,c2,c3=sorted(s)
        c1y,c1x=c1
        if ([c1y+1,c1x]==c3 and [c1y,c1x+1]==c2) or ([c1y+1,c1x-1]==c2 and [c1y+1,c1x]==c3) or ([c1y,c1x+1]==c2 and [c1y+1,c1x+1]==c3) or ([c1y+1,c1x]==c2 and [c1y+1,c1x+1]==c3):
            ch=True
            for i in s[1:]:

                ch=func2(i,s)
                if ch==False:
                    break
        if ch:
            l[y][x]='0'
            for y,x in s:
                l[y][x]='0'
            return l,True
        else:
            return l,False
    else:
        return l,False
            
def func2(coo,s):
    y,x=coo
    pt=l[y][x]
    s=s
    c=0

    for i in range(4):
        if y+dyl[i]<n and y+dyl[i]>=0 and x+dxl[i]<n and x+dxl[i]>=0:
            if pt==l[y+dyl[i]][x+dxl[i]] and [y+dyl[i],x+dxl[i]] not in s:
                c+=1

    if c==0:
        return True
    else:
        return False
                
n=int(input())

dxl=[-1,0,1,0]
dyl=[0,-1,0,1]
l=[]
for i in range(n):
    x=input().split()
    l.append(x)
c=0
for y in range(n):
    for x in range(n):
        pt=l[y][x]
        if pt!='0':
            l,ch=func(y,x,l)
            if ch:
                c+=1
print(c)
