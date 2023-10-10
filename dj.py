'''
Time: 20.00-20.30
list-music: 12
dandelions 3.50
thatthong-sound 3.55
everyday 3.55
just-curious 3.34
why 4.15
top-secret 3.54
tom-jerry 3.39
17mins 4.10
invincible-love 4.09
daze 3.53
expert 3.58
kiminoto 4.05'''

t1,t2=input().split(': ')[-1].split('-')


a,b=list(map(int,t1.split('.')))
c,d=list(map(int,t2.split('.')))

timeleft=(c-a)*3600+(d-b)*60

timeprint=a*3600+b*60

l=[]
n=int(input().split(': ')[-1])
for i in range(n):
    name,length=input().split()
    lm,ls=length.split('.')
    length=int(lm)*60+int(ls)
    l.append([length,name])
l.sort()

for song in l:
    length,name=song

    if length>timeleft:
        break
    
    timeleft-=length
    
    old=timeprint

    timeprint+=length
    total=timeprint

    h=total//3600
    total-=h*3600

    m=total//60
    total-=m*60
    s=total
    
    hold=old//3600
    old-=hold*3600
    mold=old//60
    old-=mold*60
    sold=old


    if m>=60:
        m-=60
        h+=1
    if h>=24:
        h-=24
    if mold>=60:
        mold-=60
        hold+=1
    if hold>=24:
        hold-=24
    print(f'{name} {hold:02d}:{mold:02d}-{h:02d}:{m:02d}')
    


    