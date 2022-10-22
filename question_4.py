print("Question 4: 20MIM10056")

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return 0
        
    return 1

upper = int(input("Enter the upper range: "))

for num in range(2, upper + 1):
    if(isPrime(num)):
        print(num)
       # all prime numbers are greater than 1
    