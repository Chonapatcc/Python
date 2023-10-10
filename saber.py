n=int(input())
for i in range(n):
    a=input().split()
    s=0
    c=0
    for i in a:
        if s>16 or c==5:
            break
        if i in 'A':
            s+=1
        elif i in 'KQJ':
            s+=10
        else:
            s+=int(i)
        c+=1
    if s>21:
        print('busted')
    else:
        print(s)