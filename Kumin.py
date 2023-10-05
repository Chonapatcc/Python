l='N S E W'.split()
dx=[0,0,1,-1]
dy=[1,-1,0,0]
x,y=0,0

n=input().split()
for i in n[:-1]:
    dis=''
    way=''
    c=0
    for j in i:
        if j.isdigit():
            dis+=j
        else:
            way+=j
            c+=1
    dis=int(dis)
    if c==1:
        ind=l.index(way)
        x+=dx[ind]*dis
        y+=dy[ind]*dis
    else:
        for w in way:
            if w in way:
                ind=l.index(w)
                x+=dx[ind]*dis/2**(1/2)
                y+=dy[ind]*dis/2**(1/2)
            

print(f'{x:.3f} {y:.3f}')
d=(x**2+y**2)**(1/2)
print(f'{d:.3f}')
    