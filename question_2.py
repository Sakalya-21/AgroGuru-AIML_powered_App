print("Question 2: 20MIM10056")
sum_num = 0
avg = 0
count =0

while True:
    n = int(input("Enter a Number: "))
    if(n==0): 
        break
    sum_num += n
    count +=1

avg = sum_num/count
print("The Sum of All numbers Entered is: ", sum_num)
print("The Average of all number entered is: ", avg)