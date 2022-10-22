print("Question 9: 20MIM10056")

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return 0
        
    return 1

n = int(input("Enter the value of n: "))

print("The first {} prime numbers are: ".format(n))

i=2
while(n>=1):
    if(isPrime(i)):
        print(i)
        n-=1
    i+=1

