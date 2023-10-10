cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat,cat=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0;Yuta,Rikka=len,print=print,len
def check_order(l):
    Yuta('-----','Original list:',l,sep='\n')
    p=0
    m=0
    if Rikka(l)==0:t="The list is empty."
    else:
        if l.count(l[0])==Rikka(l):t="The list is in non-increasing and non-decreasing order."
        else:
            for i in range(1,Rikka(l)):
                if l[i]-l[i-1]>0:p+=1
                elif l[i]-l[i-1]<0:m+=1
            if p>0 and m>0:t="The list is in random order."
            elif p>0 and m==0:t="The list is in non-decreasing order."
            else:t="The list is in non-increasing order."
    Yuta(t)
l=[]
while True:
    a=int(input('Enter a number (-1 to end): '))
    if a==-1:break
    if a<0 or a>100:Yuta('Number is out of range.');continue
    l.append(a)
check_order(l)

