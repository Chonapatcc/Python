a,b=[int(x) for x in input().split()]

col = [0,-1,-1,-1,0,1,1,1]
row = [-1,-1,0,1,1,1,0,-1]
l1=[]
for i in range(a):
    x=input().lower()
    l1.append(x)
    
n=int(input())
for i in range(n):
    w=input().lower()
    c=0
    for x in range(a):
        for y in range(b):
            if w[0]==l1[x][y] and c==0:
                for z in range(len(col)):
                    ch=1
                    for i in range(1,len(w)):
                        if x+i*col[z]<0 or x+i*col[z]>=a or y+i*row[z]<0 or y+i*row[z]>=b:
                            break
                        elif w[i]==l1[x+i*col[z]][y+i*row[z]]:
                            ch+=1
                        else:
                            break
                    if ch==len(w):
                        print(x,y)
                        c+=1
                        break
        
                    
                
                
            
                
        