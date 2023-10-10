n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
money=int(input())
for i in l:
    d=money//i
    money-=d*i
    print(f'{i}: {d}')
