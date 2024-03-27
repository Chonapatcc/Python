cat= []
for i in range(4):
    n=int(input())
    cat.append(n)
x1,y1,x2,y2 = cat
x = x1-x2;
y = y1-y2;

print("NO") if(x>1 or x<-1 or y>1 or y<-1) else print("YES")

    
