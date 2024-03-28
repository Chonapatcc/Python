primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

start =int(input())
stop = int(input())


for i in range(start , stop+1):
    ch =1
    for prime in primes:
        if(i%prime==0):
            ch=0
    if ch :
        print(i)