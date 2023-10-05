a1,a2=[int(x) for x in input().split()]
l1=[""]*a1
l2=[""]*a2
l=[" _ | ||_|","     |  |"," _  _||_ "," _  _| _|","   |_|  |"," _ |_  _|"," _ |_ |_|"," _   |  |"," _ |_||_|"," _ |_| _|"]# 0-9


for i in range(3):
    x=input()
    c=0
    cc=0
    while True:
        if cc==a1:
            break
        l1[cc]+=x[c:c+3]
        cc+=1
        c+=4
     
for i in range(3):
    x=input()
    c=0
    cc=0
    while True:
        if cc==a2:
            break
        l2[cc]+=x[c:c+3]
        cc+=1
        c+=4
n1=""
n2=""
for i in l1:
    n1+=str(l.index(i))
for i in l2:
    n2+=str(l.index(i))
print(int(n1)+int(n2))

        
