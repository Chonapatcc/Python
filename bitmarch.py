n=2
l=[]
x="1"*n
le=len(x)
for i in range(8-3+1):
    t='0'*(8-le-i)+x+'0'*i
    l.append([int(x) for x in list(t)])
print(l)