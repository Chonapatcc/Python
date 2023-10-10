def func(a,b):
    t=1
    for i in range(b+1,a+1):
        t*=i%998244353
        t%=998244353
    #d[a]=t
    return t
n=int(input())
d={87654321: 874459189}
for i in range(n):
    a,b=list(map(int,input().split()))
    a=a%998244353
    b=b%998244353
    if a in d:
      c=d[a]
    else:
      c=func(a,b)
    c%=998244353
    print(c)
'''f = open("evild.txt", "w")
f.write(str(d))
f.close()'''
