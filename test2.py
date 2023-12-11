xprice={}
xtime={}
high=0
hname=''

while True:
    a=input()
    if a=='end':
        break
    a,b=a.split()
    b=float(b)
    
    if a in xprice:
        xtime[a]=xtime[a]+1
        if b>xprice[a]:
            xprice[a]=b
    else:
        xprice[a]=b
        xtime[a]=1
    if b>high:
        high=b
        hname=a
k=list(xprice.keys())
k.sort()
for i in k:
    s=''
    if xtime[i]>1:
        s='s'
    print(f"{i} bid at the price of {xprice[i]:.1f} baht in {xtime[i]} time{s}.")
print(f'The winner is {hname}.')
        
    