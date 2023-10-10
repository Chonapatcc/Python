n=int(input())
w=input()
if n<0 or w.lower() not in 'eo' or (n==0 and w.lower()=='o'):
    print('ERROR')
else:
    l=[1,1]

    for i in range(1,n):
        l.append(l[i]+l[i-1])
    l=l[:n+1]
    c=0
    if w.lower()=='e':
        for i in range(len(l)):
            if i%2==0:
                c+=l[i]

    elif w.lower()=='o':
        for i in range(len(l)):
            if i%2!=0:
                c+=l[i]
    print(c)
    
    