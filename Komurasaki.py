t=input().split()[-1].split("-")
l=[]
for i in t:
    a,b=[int(x) for x in i.split(".")]
    a=a*60*60
    b=b*60
    c=b+a
    l.append(c)
st,end=l[0],l[1]
dif=end-st
n=input().split()[-1]
n=int(n)
ml=[]
for i in range(n):
    name,time=input().split()
    time=float(time)
    ml.append([time,name])
ml.sort()
c=0

for i in ml:
    time,name=i
    time=str(time)
    a,b=time.split(".")
    a=int(a)
    b=int(b)
    a=a*60
    time=b+a

    if c+time>dif:
        break
    #print(c,c+time)
    print(name,end=" ")
    s=st+c
    h=s//3600
    s=s-h*3600
    m=s//60
    s=s-m*60

    mm=round(m+s/100)

    #m=round(m)
    print(f"{int(h):02d}:{mm:02d}-",end="")
    c+=time
    s=st+c
    h=s//3600
    s=s-h*3600
    m=s//60
    s=s-m*60

    mm=round(m+s/100)
    #m=round(m)
    print(f"{int(h):02d}:{mm:02d}")


    
    
    

