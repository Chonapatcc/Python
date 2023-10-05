a=input()
b=input()
n1,n2=len(a),len(b)

m=0
l=[]

for i in range(n1):
    if n1-i-1<m:
        break
    for y in range(n2):
        if n2-y-1<m:
            break
        t=''
        tc=0
        ind=1
        if a[i]==b[y]:
            t+=a[i]
            tc+=1
            while True:
                if i+ind<n1 and y+ind<n2:
                    if a[i+ind]==b[y+ind]:
                        t+=a[i+ind]
                        tc+=1
                        ind+=1
                    else:
                        break
                else:
                    break
        if tc>m:
            m=tc
            l=[]
            l.append(t)
        elif tc==m:
            l.append(t)

print(l[0])
            
                
    
    