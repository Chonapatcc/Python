a,b=[int(x) for x in input().split()]
l1=[] #x T # 
l2=[""]*b #y T 
l3=[""]*b #diagonal top left to bot rigth  T 
l4=[""]*b #diagonal top right to bot left F
l5=[""]*b #  T
l6=[""]*b # F
c1=0

for i in range(a):
    x=input().lower()
    xx=x[::-1]
    l1.append(x)
    for y in range(b):
        l2[y]+=x[y]
        if c1+y<b:
            l3[y]+=x[c1+y]
            l4[y]+=xx[c1+y]
        else:
            l3[y]+="*"
            l4[y]+="*"
    c1+=1
l1re=l1[::-1]
c1=0
for i in l1re:
    x=i
    xx=x[::-1]
    for y in range(b):
        if c1+y<b:
            l5[y]+=x[c1+y]
            l6[y]+=xx[c1+y]
        else:
            l5[y]+="*"
            l6[y]+="*"
    c1+=1



nl4=[]
for i in l4:
    nl4.append(i[::-1])
l4=nl4
nl6=[]
for i in l6:
    nl6.append(i[::-1])
l6=nl6

print(l1,l2,l3,l4,l5,l6,sep="\n")
'''n=int(input())
for i in range(n):
    w=input().lower()
    while True:
        for y in l1:
            ww=w[::-1]
            if w in y:
                print(y.index(w))
            elif ww in y:
                print(y.index(ww))
            '''
    
    


    