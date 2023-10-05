l=[ 1, 3/4, 2/4, 1/4, 1/8]
import math
n=int(input())
old=0
s=0
for i in range(n):
    x=[int(x) for x in input().split()]
    for p in range(5):
        if x[p]*l[p]>old:
            re=math.ceil(x[p]*l[p])
            old+=re

            s+=re
            old-=x[p]*l[p]
        else:
            old-=x[p]*l[p]
            
print(s)
        