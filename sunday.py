month = {
1:31,
2:28,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31
}
d1,m1=list(map(int,input().split('-')))
d2,m2=list(map(int,input().split('-')))
fsun=int(input())
# check month and day
ch1=False
ch2=False
if m1<=0 or m2<=0 or m1>12 or m2>12:
    ch1=True
if not ch1:
    if d1>month[m1] or d2>month[m2] or d1<=0 or d2<=0 :
        ch2=True
else:
    if d1>31 or d2>31 or d1<=0 or d2<=0 or fsun>7 or fsun<=0:
        ch2=True

if ch1:
    print("Wrong Month")
if ch2:
    print("Wrong Day")
    
if not ch1 and not ch2:#month and day corrected.
    #sort value
    if m1==m2:
        if d1>d2:
            d1,d2=d2,d1
    elif m1>m2:
        d1,d2,m1,m2=d2,d1,m2,m1
    #cal
    c=0
    mon=1
    day=fsun
    while True:
        dch=month[mon]
        #print(dch,mon,day,c)
        if mon==m2 and day>d2:
            break
        if day>dch:
            mon+=1
            day=day-dch
        if mon<m1:
            day+=7
        if mon>m1 and mon<m2:
            c+=1
            day+=7
        elif mon==m1:
            if day>=d1:
                c+=1
                day+=7
            else:
                day+=7
        elif mon==m2:
            if day<=d2:
                c+=1
                day+=7
    print(c)            
    
        