print("Question 7: 20MIM10056")
print("Python program to calculate the sum of digits")

n = int(input("Enter a number: "))

temp = n
sum_digits = 0

while(n>0):
    r = n%10
    sum_digits += r
    n = n//10

print("Sum of digits of the number {} is {}".format(temp,sum_digits))
