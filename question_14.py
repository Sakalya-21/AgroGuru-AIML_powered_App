print("Question 14: 20MIM10056")

str = input("Enter a string: ")
charac = input("Enter a character: ")

print("The number of times {} occurs using count() method is:{}".format(charac,str.count(charac)))

def countChar(str,char):
    count = 0
    for i in str:
        if(i== charac):
            count+=1
    return count

print("The number of times {} occurs using custom function is:{}".format(charac,countChar(str,charac)))
