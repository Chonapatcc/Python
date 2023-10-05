t=input()
d={}
dn=0

if '(' in t:
    t=t.replace('(',' (')
    t=t.replace(')',") ")
t=t.split()

nt=""
for i in t:
    if '(' in i:
        d[dn]=i
        nt+=str(dn)
        dn+=1
    else:
        nt+=i
t=nt
print(t)

n=int(input())
for i in range(n):
    x=input().split()
    s=t
    te='p'
    for y in x:
        y=int(y)-1
        if y==-1:
            break

        opl=list("+*^")
        if s.isdigit():
            if y>=1:
                s='null'
                te=f'op({y+1},{te})'
                break
            s=d[int(s)]
        if '(' in s and ')' in s:
            s=s[1:-1]
        else:
            ch=False
            for aop in opl:
                if aop in s:
                    s=s.split(aop)
                    ch=True
                    break
            if y>=len(s):
                s='null'
                te=f'op({y+1},{te})'
                break
                
            s=s[y]
        te=f'op({y+1},{te})'
    nt=''
    for i in s:
        if i.isdigit():
            nt+=d[int(i)]
        else:
            nt+=i
    s=nt
    print(f"{te}={s}")
    
            
    
    