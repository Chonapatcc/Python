n=int(input())
x,y=0,0
st='E'
l='N E S W'.split()
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ch=False
for i in range(n):
    if ch:
        break
    w,dis=input().split()
    dis=int(dis)

    ind=l.index(st)
    if w=="LT":
        ind-=1
        st=l[ind]
    elif w=='RT':
        if ind+1==4:
            ind-=3
        else:
            ind+=1
        st=l[ind]
    elif w=='BW':
        ind-=2
        st=l[ind]
    x+=dx[ind]*dis
    y+=dy[ind]*dis
    if x<=-50000 or x>=50000 or y<=-50000 or y>=50000:
        ch=True

if ch:
    print('DEAD')
else:
    print(x,y)
    print(st)  
        

        