n=int(input())
l=[0]*256
c=0
for i in range(n):
    a=[int(x) for x in input().split()]
    c+=1
    for y in range(a[0],a[2]):
        if a[1]>l[y]:
            l[y]=a[1]


for i in range(1,256):
    if l[i]!=l[i-1]:
            print(i,l[i],end=" ")
        
        



