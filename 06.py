t=input()
ce=0
if t.count('.')>1:
    ce+=1
if not ce:
    for i in t:
        if i.isdigit()==False and i!=',' and i!='.':
            ce+=1
            break
dotl=0
if not ce:
    if '.' in t and ',' in t:
        t1,t2=t.split('.')
        dotl=len(t2)
        if ',' in t2:
            ce+=1
        if len(t2)>2:
            ce+=1
        s=t1.split(',')
        if len(s[0])>3:
            ce+=1
        for i in s[1:]:
            if len(i)!=3:
                ce+=1
        t=t.replace(',','')
    elif '.' in t:
        t1,t2=t.split('.')
        dotl=len(t2)
        if len(t2)>2:
            ce+=1
    elif ',' in t:
        t1=t.split(',')
        for i in t1[1:]:
            if len(i)!=3:
                ce+=1
        t=t.replace(',','')

if ce==0:
    tp=0
    if float(t)==int(float(t)):
        tp=int(float(t))+1
    else:
        tp=float(t)+1
    if dotl==2:
        print(f'{tp:.2f}')
    else:
        print(tp)
else:
    print('ERROR')