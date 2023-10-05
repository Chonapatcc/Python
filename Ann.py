t=input().lower()

ch1=False
ch2=False

if t==t[::-1]:
    ch1=True
    n=len(t)//2
    if len(t)%2==0:
        t1=t[:n]
        t2=t[n:]
    else:
        t1=t[:n]
        t2=t[n+1:]
    if t1==t1[::-1] and t2==t2[::-1]:
        ch2=True
p=''
if ch2 and ch1  :
    p='Double Palindrome'
elif ch1:
    p='Palindrome'
else:
    p='No'

print(p)
