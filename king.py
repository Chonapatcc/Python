
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

word = input().split(" to ")
start,stop = int(word[0]),int(word[1])


for i in range(start ,stop+1):
    cal1 = (i-1)/2
    cal2 = (i+1)/2
    #print(cal1,int(cal1),cal2,int(cal2))
    #break;
    cal = int(i**(1/2))
    ch=1;
    for y in primes:
        if i%y==0:
            ch=0
            break
    if(ch):
        for y in range(98,cal+1):
            if i%y==0:
                ch=0
                break
    if(ch):
        print(i,end=" ")