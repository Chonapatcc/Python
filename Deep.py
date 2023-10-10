import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
l=[]
for i in range(h):
    a,b=input().split()
    a=int(a)
    b,c=int(b[:-1]),b[-1]
    l.append([a,b,c])
l.sort()
l=l[::-1]
have=0

for a,b,c in l:
    have+=a*b




for a,b,c in l:
    cal=a*100

    if have>=cal:
        have-=cal
        print(f"{a} 100%")
    elif have>0:
        per=have//a
        have=0
        print(f"{a} {per}%")
    
'''
2
100 90%
100 30%'''