n=input()

l='- _ = . $'.split()
for i in l:
    n=n.replace(i,' ')



n=n.split(' ')
old=''
for i in n:
    if i!='':
        old=i
        break
t=n[0].lower()

for i in n[1:]:
    i=i.capitalize()
    t+=i
if n[0]=='':
    if len(n)==n.count(''):
        print('')
    else:
        t=t[0].lower()+t[1:]
        print(t)
else:
    print(t)